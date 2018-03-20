from django.shortcuts import render
import requests
import plotly.offline as opy
import plotly.graph_objs as go
# Create your views here.


def forecast(city):
    URL = 'http://api.openweathermap.org/data/2.5/forecast'
    param = dict(
        q=str(city+',in'),
        APPID='5227a9d5565d2655fbf1539be0797d09',
    )
    a = requests.get(URL, params=param)
    print(a.json())
    return a.content


def forecastview(request,**kwargs):
    print('calling view forecast')
    context = dict()
    context['obj'] = forecast('Coimbatore')
    print(context['obj'])

    return render(request, 'forecast.html', context)
