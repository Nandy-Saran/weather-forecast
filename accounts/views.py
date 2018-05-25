from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect,HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
import datetime
from accounts.forms import SubscriberForm, NoCurForm, sms_crop_form
from accounts.models import Subscriber
from accounts.tokens import account_activation_token
from datamodel.models import Crop, Weather,Place
from datamodel.models import disPest, Pesticide
#from accounts.models import sms_farmer
from utilities.send_sms import *

# Create your views here.

@login_required
def subscriberView(request, **kwargs):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            print(obj)
            print(obj.currentCrop)
            if obj.currentCrop:
                print('no recomm')
                obj.isCurFarm=True
                obj.save()
                return redirect('home1')
            elif not obj.prevCrop:
                print('Not having previous crop')
                obj.save()
                return redirect('home2')
            elif obj.prevCrop:
                print('Having previous crop')
                return redirect('reCommCrop')
    else:
        form = SubscriberForm()
    form.fields['user'].initial = request.user
    return render(request, 'subscriber.html', {'form': form})


@login_required
def newsubscView(request):
    if request.method == "POST":
        form = NoCurForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=True)
            return redirect('home2')
    else:
        form=NoCurForm()
    form.fields['user'].initial=request.user
    return render(request,'subscriber.html',{'form':form})


def signup(request):
    if request.method == 'POST':
        aadhar_number = request.POST['aadhar']
        farmer_name = request.POST['fname']
        password = request.POST['pin']

        user_instance = User.objects.create_user(username=aadhar_number, password=password)
        user_instance.first_name = farmer_name
        user_instance.save()

        return HttpResponseRedirect('/login/')

    return render(request, 'signup.html')

def user_login(request):
    if request.method == "POST":
        aadhar_number = request.POST['aadhar']
        password = request.POST['pin']

        user = authenticate(username=aadhar_number, password=password)
        if user is not None:
            login(request, user)
            try:
                subIns=Subscriber.objects.get(user=user)
                if subIns.currentCrop:
                    return HttpResponseRedirect('home1')
                elif subIns.prevCrop:
                    return HttpResponseRedirect('home2')
            except:
                print('Excepted')
                return HttpResponseRedirect('wayToForm')
        return HttpResponseRedirect('subscriberView')
    return render(request, 'login.html')


def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')

def wayToForm(request):
    return render(request,'WayToForm.html') 


@login_required
def home1(request):
    instanc = Subscriber.objects.get(user=request.user)
    print(instanc.location)
    WeathObj = Weather.objects.filter(place=instanc.location).filter(datenum__gte=0)
    dic = {}
    dic['yield_com']=False
    dic['Recom']=False
    dic['Picmes']=False
    dic['avail'] = True
    dic['ElecConduc']=instanc.ElecConduc-instanc.currentCrop.ElecConduc
    dic['OrgCarbonP']=instanc.OrgCarbonP-instanc.currentCrop.OrgCarbonP
    dic['Nitrogenkgha']=instanc.Nitrogenkgha-instanc.currentCrop.Nitrogenkgha
    dic['Phosphoruskgha']=instanc.Phosphoruskgha-instanc.currentCrop.Phosphoruskgha
    dic['Potassium_kgha']=instanc.Potassium_kgha-instanc.currentCrop.Potassium_kgha
    dic['Sulphur_ppm']=instanc.Sulphur_ppm-instanc.currentCrop.Sulphur_ppm
    dic['Zinc_ppm']=instanc.Zinc_ppm-instanc.currentCrop.Zinc_ppm
    dic['Boron_ppm']=instanc.Boron_ppm-instanc.currentCrop.Boron_ppm
    dic['Ironppm']=instanc.Ironppm-instanc.currentCrop.Ironppm
    dic['Manganese_ppm']=instanc.Manganese_ppm-instanc.currentCrop.Manganese_ppm
    dic['Copper_ppm']=instanc.Copper_ppm-instanc.currentCrop.Copper_ppm
    dic['Waterph']=instanc.Waterph-instanc.currentCrop.Waterph

    instanc.pHadv=instanc.picMsg=instanc.cropmes=instanc.recCrop=''
    Forecast = []
    comm = ''
    lis2 = lis3 =[]
    if instanc.currentCrop.pH_min and instanc.currentCrop.pH_min > instanc.soil_ph:
        comm += 'Cultivate your crop according to your soil pH\nYour crop' + instanc.currentCrop.name + 'requires soil with pH range from' + str(
            instanc.currentCrop.pH_min) + ' to ' + str(instanc.currentCrop.pH_max)
    if instanc.currentCrop.pH_min and instanc.currentCrop.pH_max < instanc.soil_ph:
        comm += 'Cultivate your crop according to your soil pH\nYour crop' + instanc.currentCrop.name + 'requires soil with pH range from' + str(
            instanc.currentCrop.pH_min) + ' to ' + str(instanc.currentCrop.pH_max)
    instanc.pHadv=comm
    FerAd=instanc.currentCrop.ferAdv
    IrrAd=instanc.currentCrop.irrAdv
    dic['ferAdv']=FerAd
    dic['IrrAdv']=IrrAd

    Picmsg = ''
    if instanc.currentCrop.pick_start and instanc.datOfSow:
        print(str(instanc.datOfSow)+'this is date of sow')
        dic3={1:'Yesterday',0:'Today',2:'Day before yesterday'}
        datdiff=datetime.date.today()-instanc.datOfSow
        det=datdiff.days-instanc.currentCrop.pick_start
        print(datdiff,det)
        if instanc.currentCrop.interv:
            if det>0:
                if (det//instanc.currentCrop.interv)<instanc.currentCrop.count:
                    count=det//instanc.currentCrop.interv
                    Picmsg = 'You should have completed ' + str(count - 1) + 'th harvest and have to do ' + str(
                        count) + 'th pick'
                else:
                    Picmsg='Please enter the total yield if processes are completed'
                    dic['yield_com']=True
            elif det>-3:
                Picmsg = 'You have to start first harvest in' + dic3[det]
            else:
                Picmsg = 'You have to start first harvest in ' + str(det * -1) + ' days'
        else:
            if det>0 and det<4:
                Picmsg='You should have started the picking before '+str(det)+' days'
            elif det>-3:
                Picmsg='You have to start first pick in'+dic3[det]
            else:
                Picmsg='You have to start first pick in '+str(det*-1)+' days'
        dic['Picmes']=True
    else:
        dic['yield_com']=True
    dic['Picmsg']=Picmsg
    instanc.picMsg=Picmsg
    PesInst = disPest.objects.get(crop=instanc.currentCrop)

    for Pstc in PesInst.pest.all():
        dic2={}
        print(Pstc.pestname)
        dic2['Pest'] = Pstc.pestname
        print(Pstc.pesticide)
        dic2['Pesticide'] = Pstc.pesticide
        lis2.append(dic2)
    for Dis in PesInst.disease.all():
        dic2 = {}
        print(Dis.diseaseName,Dis.Symptoms,Dis.Remedy)
        dic2['disease'] = Dis.diseaseName
        dic2['symptoms'] = Dis.Symptoms
        dic2['remedy'] = Dis.Remedy
        lis3.append(dic2)
    hotcount=0
    cldcount=0
    hotlis=[]
    cldlis=[]
    for i in WeathObj:
        daily = {}
        daily['desc'] = i.WindDesc
        daily['max_temp'] = i.mintempC
        daily['min_temp'] = i.maxtempC
        daily['humid'] = i.humidity
        daily['rainMM'] = i.rainMM
        daily['sunrise'] = i.sunrise
        daily['sunset'] = i.sunset
        daily['moonrise'] = i.moonrise
        daily['moonset'] = i.moonset
        daily['pressure'] = i.pressure
        daily['windspMil'] = i.WindSpeedMil
        daily['windGstMil'] = i.WindGustMil
        daily['date'] = i.date
        daily['datenum'] = i.datenum
        daily['WindDirdeg'] = i.WindDirdeg
        daily['WinddirPt'] = i.Winddir16Point
        msg1=message=''
        if instanc.currentCrop.MintempC and instanc.currentCrop.MintempC < i.mintempC:
            cldcount+=1
            cldlis.append(i.date)   
            message += 'Your Crop ' + instanc.currentCrop.name + ' may get affected due to cold temperature(' + str(
                i.mintempC) + ' deg C) in' + str(i.datenum) + 'day(s)\n'
        if instanc.currentCrop.MaxtempC and instanc.currentCrop.MaxtempC > i.maxtempC:
            hotcount+=1
            hotlis.append(i.date)   
            message += 'Your Crop ' + instanc.currentCrop.name + ' may get affected due to high temperature( ' + str(
                i.maxtempC) + ' deg C) in' + str(i.datenum) + 'day(s)\n'
        Forecast.append(daily)
    if hotcount!=0 and cldcount!=0:
        msg1+='Your Crop may get affected due to cold temperature for '+str(cldcount)+' days\n'
        for inss in cldlis:
            msg1+=str(inss)+','
        msg1+='\nAnd due to high temperature for '+str(hotcount)+' days'
        for inss in hotlis:
            msg1+=str(inss)+','
    elif hotcount!=0:
        msg1+='Your Crop may get affected due to high temperature for '+str(hotcount)+' days\n'
        for inss in hotlis:
            msg1+=str(inss)+','
    elif cldcount!=0:
        msg1+='Your Crop may get affected due to cold temperature for '+str(cldcount)+' days\n'
        for inss in cldlis:
            msg1+=str(inss)+','
    Forecast.append(daily)
    dic['mesg']=msg1
    instanc.cropmes=dic['mesg']
    dic['data'] = Forecast
    dic['advice'] = comm
    print(dic['data'])
    dic1 = {}
    totinst = Subscriber.objects.filter(location=instanc.location).filter(isCurFarm=True)
    req = {}
    for i in totinst:
        flag = 0
        for j in dic1:
            if j == i.currentCrop:
                dic1[j] += 1
                flag = 1
                break
        if flag == 0:
            dic1[i.currentCrop] = 1
    lis = sorted(dic1, key=lambda k: dic1[k])
    count = 0
    for a in lis:
        if a != instanc.currentCrop:
            ins = Crop.objects.get(name=a)
            if ins.pH_min and ins.pH_min > instanc.soil_ph and ins.pH_max and ins.pH_max < instanc.soil_ph:
                req['crop'] = a
                st = ins.seas_no
                seas = ''
                if st.find('-') != -1:
                    req['season'] = 'Any month from January to December'
                else:
                    dicsp = {1: 'January', 2: 'Febraury', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July',
                             8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
                    ar = st.split(',')
                    for x in ar:
                        seas += dicsp[x] + ','
                    req['season'] = seas
                count += 1
                dic['Recom']=True
                dic['required'] = 'Recommended Crop is ' + req['crop'] + ' during ' + req['season'] + ':Season'

                instanc.recCrop=dic['required']
                break
    
    dic['pestdet'] = lis2
    dic['disDet'] = lis3
    print(instanc.Mobile_no, dic['Picmsg'])
    #send_sms(dic['Picmsg'], 'hi', instanc.Mobile_no)
    #send_sms(dic['Picmsg'], 'ta', instanc.Mobile_no)
    # send_sms(dic['Picmsg'], 'ma', instanc.Mobile_no)
    #print(lis2)
    print(dic)
    print(req)
    template = loader.get_template('home1.html')
    context = {'forecast': dic}
    return render(request, 'home1.html', context)

def home2(request):
    instanc = Subscriber.objects.get(user=request.user)
    difference={}
    for i in Crop.objects.all():
        difference[i]=0
    for CropIns in Crop.objects.all():
        print(instanc.ElecConduc,CropIns.ElecConduc)
        if not instanc.soil_ph>=CropIns.pH_min and instanc.soil_ph<=CropIns.pH_max:
            if instanc.soil_ph<CropIns.pH_min:
                difference[CropIns]+=2*(CropIns.pH_min-instanc.soil_ph)
            else:
                difference[CropIns]+=2*(instanc.soil_ph-CropIns.pH_max)
        difference[CropIns] += abs(instanc.ElecConduc - CropIns.ElecConduc)
        difference[CropIns] += abs(instanc.OrgCarbonP - CropIns.OrgCarbonP)
        difference[CropIns] += abs(instanc.Nitrogenkgha - CropIns.Nitrogenkgha)
        difference[CropIns] += abs(instanc.Phosphoruskgha - CropIns.Phosphoruskgha)
        difference[CropIns] += abs(instanc.Potassium_kgha - CropIns.Potassium_kgha)
        difference[CropIns] += abs(instanc.Sulphur_ppm - CropIns.Sulphur_ppm)
        difference[CropIns] += abs(instanc.Zinc_ppm - CropIns.Zinc_ppm)
        difference[CropIns] += abs(instanc.Boron_ppm - CropIns.Boron_ppm)
        difference[CropIns] += abs(instanc.Ironppm - CropIns.Ironppm)
        difference[CropIns] += abs(instanc.Manganese_ppm - CropIns.Manganese_ppm)
        difference[CropIns] += abs(instanc.Copper_ppm - CropIns.Copper_ppm)
        difference[CropIns] += abs(instanc.Waterph - CropIns.Waterph)
    sorted(difference, key=lambda k:difference[k],reverse=True)
    recCrlis1=[]
    count=0
    Reclis=[]
    dicsp = {1: 'January', 2: 'Febraury', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July',
             8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    for i in difference:
        j={}
        if count==6:
            break
        print(i)
        print(i.ElecConduc-instanc.ElecConduc)
        try:
            Instances=Subscriber.objects.filter(location=instanc.location).filter(isCurFarm=True).filter(currentCrop=i)
        except:
            print('What')
        cnt=0
        for k in Instances:
            cnt+=1
        j['pH']=0
        if not instanc.soil_ph>=i.pH_min and instanc.soil_ph<=i.pH_max:
            if instanc.soil_ph<i.pH_min:
                j['pH']=instanc.soil_ph-i.pH_min
            else:
                j['pH']=instanc.soil_ph-i.pH_max
        j['count']=cnt
        j['crop']=i
        j['Elec']=i.ElecConduc-instanc.ElecConduc
        j['OrgCar']=i.OrgCarbonP-instanc.OrgCarbonP
        j['Nitrogen']=i.Nitrogenkgha-instanc.Nitrogenkgha
        j['Phosphorus']=i.Phosphoruskgha-instanc.Phosphoruskgha
        j['Potassium']=i.Potassium_kgha-instanc.Potassium_kgha
        j['Sulphur']=i.Sulphur_ppm-instanc.Sulphur_ppm
        j['Zinc']=i.Zinc_ppm-instanc.Zinc_ppm
        j['Boron']=i.Boron_ppm-instanc.Boron_ppm
        j['Iron']=i.Ironppm-instanc.Ironppm
        j['Manganese']=i.Manganese_ppm-instanc.Manganese_ppm
        j['Copper']=i.Copper_ppm-instanc.Copper_ppm
        j['Water_pH']=i.Waterph-instanc.Waterph
        st = i.seas_no
        seas = ''
        if st.find('-') != -1:
            seas = 'Any month from January to December'
        else:
            ar = st.split(',')
            for x in ar:
                seas += dicsp[int(x)] + ','
        j['Seasons']=seas
        Reclis.append(j)    
        count+=1
    recCrlis1=sorted(Reclis ,key=lambda crop:crop['count'])
    print(recCrlis1)
    context = {'CropList': recCrlis1}
    print(context)
    return render(request, 'recommendation.html', context)

def created(request):
    if request.method =='POST':
        inst=request.POST.get('stat1')
        instanc=Subscriber.objects.get(user=request.user)
        crIns=Crop.objects.get(name=inst)
        print(crIns.name+'This is the updated crop')
        instanc.currentCrop=crIns
        instanc.datOfSow=datetime.date.today()
        instanc.isCurFarm=True
        instanc.save()
        st='Successful'
        return render(request,'welcome.html',context={'message':st})
    st='Failure'
    return render(request,'welcome.html',context={'message':st})

@login_required()
def reCommCrop(request):
    instanc=Subscriber.objects.get(user=request.user)
    totinst = Subscriber.objects.filter(location=instanc.location).filter(isCurFarm=True)
    for i in totinst:
        print(i.name)
    dic1 = {}
    CropL=[]
    SeasL=[]
    for i in totinst:
        flag = 0
        for j in dic1:
            if j == i.currentCrop:
                dic1[j] += 1
                flag = 1
                break
        if flag == 0:
            dic1[i.currentCrop] = 1
    lis = sorted(dic1, key=lambda k: dic1[k])
    count = 0
    for i in lis:
        print(i.Nitrogenkgha)
    print('entered loop')
    print(dic1)
    dicd={}
    dicd['exist']=False
    for a in dic1:
        print(a.Nitrogenkgha)
        if count<5:
            try:
                ins = Crop.objects.get(name=a.name)
                print('1')
                if ins.pH_min and ins.pH_min > instanc.soil_ph and ins.pH_max and ins.pH_max < instanc.soil_ph:
                    dicd['exist']=True
                    print('satisfied')
                    count+=1
                    CropL.append(a)
                    st = ins.seas_no
                    seas = ''
                    if st.find('-') != -1:
                        seas = 'Any month from January to December'
                    else:
                        dicsp = {1: 'January', 2: 'Febraury', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July',
                                 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
                        ar = st.split(',')
                        for x in ar:
                            seas += dicsp[x] + ','
                    SeasL.append(seas)
                    count += 1
                print('2')
            except:
                print('Wrong')
        else:
            break
        print('4')
    RecAdv="Recommed Crop(s) are:\n"
    print('5',CropL,SeasL)
    SeasL.append('Any Month fron Aud jk')
    CropL.append(Crop.objects.get(name='Brinjal'))
    dic3={}
    dicd['CropSeaslist']=[]
    dicd['exist']=True
    for i,j in zip(CropL,SeasL):
        print(i,j)
        RecAdv+=str(i)+' during '+j+':Season\n'
        dic3['crop']=i
        dic3['Seas']=j
        dicd['CropSeaslist'].append(dic3)
    instanc.recCrop=RecAdv
    print('6')
    instanc.save()
    return render(request,'recommendation.html',context={'Rec':dicd})



@login_required()
def home(request):
    return render(request, 'home.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')


def fill_profile(request):
    if request.method == 'POST':
        form = (request.POST)
        if form.is_valid():
            print('checked')
            pass
    else:
        form = ''
        pass


@login_required
def sms_view(request, **kwargs):
    current = request.user
    try:
        if Subscriber.objects.get(user=current):
            print('success')
            pass

    except Exception as e:
        print(e)

        return redirect('subscriberView')

    subscribed = sms_farmer.objects.filter(farmer=current)
    context = {'sub': subscribed}
    form = sms_crop_form()
    form.fields['user'].initial = request.user
    context['form'] = form
    if request.method == 'POST':
        form = sms_crop_form(request.POST)
        if form.is_valid():
            print('checked')
            obj = form.commit(False)
            print(obj)
            return render(request, 'sub_crops.html', context)
    else:
        form = sms_crop_form()
        context['form'] = form

    return render(request, 'sub_crops.html', context)

'''
def crop(request):
    obj = Subscriber.objects.get(user=request.user)
    cropIns = Crop.objects.get(name=obj.currentCrop.name)
    dic = []
    Pesobj = disPest.objects.fiter(crop=cropIns)
    for i in Pesobj:
        dic1 = {}
        PestcObj = Pesticide.objects.get(pest=i)
        dic1['Pest'] = i.name
        dic1['Pesticide'] = PestcObj.pesticide
        dic.append(dic1)
    return render(request, 'cropPests.html', context={'dic': dic})


def homezz(request):
    return  render(request, 'homezz.html')'''
