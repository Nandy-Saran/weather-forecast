from datamodel.models import Place, Weather, State
import requests
import json

obj = State.objects.filter(name='Tamil Nadu')

objec = Place.objects.filter(state=obj)
URL1 = 'http://api.worldweatheronline.com/premium/v1/weather.ashx?key=8d1e6be726e24779bc3203822181303&q='
URL2 = ',in&num_of_days=15&tp=24&format=json'
for j in objec:
    if j.name.find(' ') != -1:
        DistrNam = j.name
        DistrNam.replace(' ', '+')
    else:
        DistrNam = j.name
    URL = URL1 + DistrNam + URL2
    try:
        a = requests.get(URL).json()
        print(a['data']['request'][0]['query'])
        strr = a['data']['request'][0]['query']
        ind = a['data']['request'][0]['query'].find(',')
        if strr[:ind] != j.name:
            print('***************This is not correct forecast**************************')

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
obj = State.objects.get(name='Andhra Pradesh')
objec = Place.objects.filter(state=obj)
URL1 = 'http://api.worldweatheronline.com/premium/v1/weather.ashx?key=8d1e6be726e24779bc3203822181303&q='
URL2 = ',in&num_of_days=15&tp=24&format=json'
for j in objec:
    if j.name.find(' ') != -1:
        DistrNam = j.name
        DistrNam.replace(' ', '+')
    else:
        DistrNam = j.name
    URL = URL1 + DistrNam + URL2
    try:
        a = requests.get(URL).json()
        print(a['data']['request'][0]['query'])
        if a['data']['request'][0]['query'] != j.name:
            print('***************This is not correct forecast**************************')

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
