from django.shortcuts import render
from datamodel.models import Crop, Weather, Place,State
from django.template import loader
# Create your views here.
from django.http import HttpResponse


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
                    DistrictList.append(temp)

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

                for k in CropObj:
                    if k.MintempC and i.mintempC < k.MintempC:
                        message += 'Your Crop ' + k.name + ' may get affected due to cold temperature(' + str(
                            i.mintempC) + ' deg C) in' + str(i.datenum) + 'day(s)\n'
                    elif k.MaxtempC and i.maxtempC > k.MaxtempC:
                        message += 'Your Crop ' + k.name + ' may get affected due to high temperature( ' + str(
                            i.maxtempC) + ' deg C) in' + str(i.datenum) + 'day(s)\n'
                daily['message'] = message
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
