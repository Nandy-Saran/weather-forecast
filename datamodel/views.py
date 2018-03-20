from django.shortcuts import render
from datamodel.models import Crop,Weather,Place
from django.template import loader
# Create your views here.
from django.http import HttpResponse


def start(request):
    return render(request,"index.html")


def index(request):
    if request.method=='POST':
        placObj=Place.objects.all()
#        WeatObj=Weather.objects.filter(name=placObj.name).filter(datenum=0)
#        for i in WeatObj:
#            if i.date!=str(Date.now()):
#                return
        for placOb in placObj:
            WeathObj=Weather.objects.filter(place__name=placOb.name).filter(datenum__gte=0)
        CropObj=Crop.objects.all()
        dic={}
        dic['avail']=True
        Forecast=[]
        message=''
        for i in WeathObj:
            daily={}
            daily['desc']=i.WindDesc
            daily['max_temp']=i.mintempC
            daily['min_temp']=i.maxtempC
            daily['humid']=i.humidity
            daily['rainMM']=i.rainMM
            daily['sunrise']=i.sunrise
            daily['sunset']=i.sunset
            daily['moonrise']=i.moonrise
            daily['moonset']=i.moonset
            daily['pressure']=i.pressure
            daily['windspMil']=i.WindSpeedMil
            daily['windGstMil']=i.WindGustMil
            daily['date']=i.date
            daily['datenum']=i.datenum
            daily['WindDirdeg']=i.WindDirdeg
            daily['WindditPt']=i.Winddir16Point
            daily['num']=i.datenum
            Forecast.append(daily)
            for k in CropObj:
                if i.mintempC<k.MintempC:
                    message+='Your Crop'+k.name+'may get affected due to cold temperature('+i.mintempC+' deg C) in'+i.datenum+'day(s)\n'
                elif i.maxtempC>k.MaxtempC:
                    message+='Your Crop'+k.name+'may get affected due to high temperature('+i.maxtempC+' deg C) in'+i.datenum+'day(s)\n'
        dic['datas']=Forecast
        template = loader.get_template('index1.html')
        context={'forecast':Forecast,'message':message}
        return HttpResponse(template.render(context, request))
 
    placObj=Place.objects.all()
    lis=[]
    for i in placObj:
        lis.append(i.name)
    template = loader.get_template('index1.html')
    context={'Placelist':lis}
    return HttpResponse(template.render(context,request))

	    
        
