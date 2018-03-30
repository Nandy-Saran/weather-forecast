from django.shortcuts import render
from datamodel.models import Crop, Weather, Place,State
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from accounts.models import Subscriber
import requests
import datetime
from django.http import JsonResponse


def start(request):
    return render(request, "index.html")


# placOb1=placOb['dept']
        # print(request.POST)
        #        WeatObj=Weather.objects.filter(name=placObj.name).filter(datenum=0)
        #        for i in WeatObj:
        #            if i.date!=str(Date.now()):
        #                return
        #for placOb in placObj:
        #    print(placOb)
def crop_advices(request):
    if request.method == 'POST':
        if request.is_ajax():
            print('***********************Success*********************')
            if request.POST.get('action') == 'getDistricts':
                print('***********************Success*********************')
                State1 = request.POST.get('state')
                DistrictList = []
                for district in Place.objects.filter(state__name=State1):
                    DistrictList.append(district)

                dictionary = {}
                dictionary['districtList'] = DistrictList

                return JsonResponse(dictionary)
       
        if 'place' in request.POST:
  
            plac=request.POST.get('place')
        
            WeathObj = Weather.objects.filter(place__name=plac)  # .filter(datenum__gte=0)
            CropObj = Crop.objects.all()
            dic = {}
            dic['avail'] = True
            Forecast = []
            for i in WeathObj:
                daily = {}
                message = ''
                print(i.WindDesc)
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
                msg1=''
                for k in CropObj:
                    hotcount=0
                    cldcount=0
                    cldlis=hotlis=[]
                    if k.MintempC and i.mintempC < k.MintempC:
                        cldcount+=1
                        cldlis.append(i.date) 
                        message += 'Your Crop ' + k.name + ' may get affected due to cold temperature(' + str(
                            i.mintempC) + ' deg C) in' + str(i.datenum) + 'day(s)\n'
                    elif k.MaxtempC and i.maxtempC > k.MaxtempC:
                        hotcount+=1
                        hotlis.append(i.date) 
                        message += 'Your Crop ' + k.name + ' may get affected due to high temperature( ' + str(
                            i.maxtempC) + ' deg C) in' + str(i.datenum) + 'day(s)\n'
                    if hotcount!=0 and cldcount!=0:
                        msg1+='Your Crop ' + k.name + ' may get affected due to cold temperature for '+str(cldcount)+' days\nAnd due to high temperature for '+str(hotcount)+' days'
                    elif hotcount!=0:
                        msg1+='Your Crop ' + k.name + ' may get affected due to high temperature for '+str(hotcount)+' days\n'
                    elif cldcount!=0:
                        msg1+='Your Crop ' + k.name + ' may get affected due to cold temperature for '+str(cldcount)+' days\n'
                daily['message']=msg1
                Forecast.append(daily)
            dic['datas'] = Forecast
            template = loader.get_template('crop_advices.html')
            context = {'forecast': dic}
            print(context)

            return HttpResponse(template.render(context, request))

    statObj = State.objects.all()
    lis = []
    for i in statObj:
        print(i.name)
        lis.append(i)
    template = loader.get_template('crop_advices.html')
    context = {'Statelist': lis}
    print(context)
    return HttpResponse(template.render(context, request))

def initiatDaily(request):
    weathObj=Weather.objects.filter(date_num=0)
    for i in weathObj:
        i.date_num=-1
    weathObj=Weather.objects.filter(date_num__gt=0)
    for i in weathObj:
        i.delete()
    lis=['Tamil Nadu','Kerala','Karnataka','Puducherry']
    obj=State.objects.get(name__in=lis)
    for obj1 in obj:
        objec = Place.objects.filter(state=obj1)
        URL1 = 'http://api.worldweatheronline.com/premium/v1/weather.ashx?key=8d1e6be726e24779bc3203822181303&q='
        URL2 = ',in&num_of_days=15&tp=24&format=json'
        for j in objec:
            if j.name.find(' ')!=-1:
                DistrNam=j.name
                DistrNam.replace(' ','+')
            else:
                DistrNam=j.name
            URL = URL1 + DistrNam + URL2
            try:
                a = requests.get(URL).json()
                print(a['data']['request'][0]['query'])
                strr=a['data']['request'][0]['query']
                ind=a['data']['request'][0]['query'].find(',')
                if strr[:ind]!=j.name:
                    print('***************This is not correct forecast**************************')
                else:

                    for i in range(14):
                        print(a['data']['weather'][i]['date'])
                        c = Weather.objects.create(place=j, date=a['data']['weather'][i]['date'], datenum=i,
                                               moonrise=a['data']['weather'][i]['astronomy'][0]['moonrise'],
                                               moonset=a['data']['weather'][i]['astronomy'][0]['moonset'],
                                               sunrise=a['data']['weather'][i]['astronomy'][0]['sunrise'],
                                               sunset=a['data']['weather'][i]['astronomy'][0]['sunset'],
                                               maxtempC=a['data']['weather'][i]['maxtempC'],
                                               mintempC=a['data']['weather'][i]['mintempC'],
                                               rainMM=a['data']['weather'][i]['hourly'][0]['precipMM'],
                                               pressure=a['data']['weather'][i]['hourly'][0]['pressure'],
                                               humidity=a['data']['weather'][i]['hourly'][0]['humidity'],
                                               WindSpeedMil=a['data']['weather'][i]['hourly'][0]['windspeedMiles'],
                                               WindGustMil=a['data']['weather'][i]['hourly'][0]['WindGustMiles'],
                                               Winddir16Point=a['data']['weather'][i]['hourly'][0]['winddir16Point'],
                                               WindDesc=a['data']['weather'][i]['hourly'][0]['weatherDesc'][0]['value'],
                                               WindDirdeg=a['data']['weather'][i]['hourly'][0]['winddirDegree'])
            except Exception as e:
                print(e)
                pass

def initDB(request):
    locQuer=Place.objects.all()
    for ins1 in locQuer:
        print(ins1)
        totinst = Subscriber.objects.filter(location=instanc.location).filter(isCurFarm=True)
        WeathObj = Weather.objects.filter(place=instanc.location).filter(datenum__gte=0)
        for instanc in Subscriber.objects.filter(location=ins1):
            instanc.cropmes=instanc.recCrop=''
            Picmsg=comm = ''
            if instanc.currentCrop.pH_min and instanc.currentCrop.pH_min > instanc.soil_ph:
                comm += 'Cultivate your crop according to your soil pH\nYour crop' + instanc.currentCrop.name + 'requires soil with pH range from'+str(instanc.currentCrop.pH_min) + ' to ' + str(instanc.currentCrop.pH_max)
            if instanc.currentCrop.pH_min and instanc.currentCrop.pH_max < instanc.soil_ph:
                comm += 'Cultivate your crop according to your soil pH\nYour crop' + instanc.currentCrop.name + 'requires soil with pH range from' + str(instanc.currentCrop.pH_min) + ' to ' + str(instanc.currentCrop.pH_max)
            instanc.pHadv=comm
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
                            Picmsg='You should have completed '+str(count-1)+'th pick and have to do '+str(count)+'th pick'
                        else:
                            Picmsg='Please enter the total yield if processes are completed'
                    elif det>-3:
                        Picmsg='You have to start first pick in'+dic3[det]
                    else:
                        Picmsg='You have to start first pick in '+str(det*-1)+' days'
                else:
                    if det>0 and det<4:
                        Picmsg='You should have started the picking before '+str(det)+' days'
                    elif det>-3:
                        Picmsg='You have to start first pick in'+dic3[det]
                    else:
                        Picmsg='You have to start first pick in '+str(det*-1)+' days'
            instanc.picMsg=Picmsg
            print(Picmsg)
            hotcount=0
            cldcount=0
            hotlis=[]
            cldlis=[]
            for i in WeathObj:
                if instanc.currentCrop.MintempC and instanc.currentCrop.MintempC < i.mintempC:
                    cldcount+=1
                    cldlis.append(i.date)
                if instanc.currentCrop.MaxtempC and instanc.currentCrop.MaxtempC > i.maxtempC:
                    hotcount+=1
                    hotlis.append(i.date)
            if hotcount!=0 and cldcount!=0:
                instanc.cropmes='Your Crop may get affected due to cold temperature for '+str(cldcount)+' days\nAnd due to high temperature for '+str(hotcount)+' days'
            elif hotcount!=0:
                instanc.cropmes='Your Crop may get affected due to high temperature for '+str(hotcount)+' days\n'
            elif cldcount!=0:
                instanc.cropmes='Your Crop may get affected due to cold temperature for '+str(cldcount)+' days\n'
            dic1 = {}
            req = {}
            for i in totinst:
                flag = 0
                for j in dic1:
                    if j == instanc.currentCrop:
                        dic1[j] += 1
                        flag = 1
                        break
                if flag == 0:
                    dic1[instanc.currentCrop] = 1
            lis = sorted(req, key=lambda k: dic1[k])
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
                        instanc.recCrop='Recommended Crop is '+req['crop']+' during '+req['season']+':Season'
                        break
            print(req)


def CalCropAr(request):
    for plInst in Place.objects.all():
        dic1={}
        for subSr in Subscriber.objects.filter(location=plInst).filter(isCurFam=True):
            flag = 0
            for j in dic1:
                if j == subSr.currentCrop:
                    dic1[j] += subSr.land_ha
                    flag = 1
                    break
            if flag == 0:
                dic1[subSr.currentCrop] = subSr.land_ha
        lis = sorted(dic1, key=lambda k: dic1[k])
        text=''
        for i in dic1:
            text += i+':'+str(dic1[i])+','
        plInst.cropList=text[:-1]

