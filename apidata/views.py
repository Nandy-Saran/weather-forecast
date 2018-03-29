from django.shortcuts import render
import requests
import plotly.offline as opy
import plotly.graph_objs as go
from django.views.generic import TemplateView
from twilio.rest import Client


# Create your views here.


def forecast(city='Coimbatore'):
    URL = 'http://api.openweathermap.org/data/2.5/forecast'
    param = dict(
        q=str(city + ',in'),
        APPID='5227a9d5565d2655fbf1539be0797d09',
    )
    a = requests.get(URL, params=param)
    print(a.json())
    return a.json()


def your_view(request):
    ''' This could be your actual view or a new one '''
    # Your code
    if request.method == 'GET':  # If the form is submitted

        search_query = request.GET.get('search_box', None)
        # Do whatever you need with the word the user looked for
        print(search_query)

    # Your code


class Graph(TemplateView):
    template_name = 'graph.html'

    def get_context_data(self, **kwargs):
        x = forecast()

        TWILIO_ACCOUNT_SID = 'AC5b2974923534e7c0a1425e68cb0fface'

        TWILIO_AUTH_TOKEN = 'e7d7eb3b1beafa02c3ca2aefa2fd8a8f'

        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        msg = client.api.account.messages.create(
            to="+919488608282",
            from_="+18312222084",
            body="hello"
        )
        print(msg.sid)

        context = super(Graph, self).get_context_data(**kwargs)
        c_name = x['city']['name']
        z = []
        d = []
        for i in range(x['cnt']):
            tem = x['list'][i]['main']['temp']
            date = x['list'][i]['dt_txt']
            z.append(tem)
            d.append(date)
        print(z, d)
        trace1 = go.Scatter(x=d, y=z, marker={'color': 'red', 'symbol': 104, 'size': "10"},
                            mode="lines", name='1st Trace')
        data = go.Data([trace1])
        layout = go.Layout(title=str(c_name + ' temperature'), xaxis={'title': 'date'}, yaxis={'title': 'temperature'})
        figure = go.Figure(data=data, layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div')
        context['graph'] = div
        c_name = x['city']['name']
        z = []
        d = []
        for i in range(x['cnt']):
            try:
                tem = x['list'][i]['rain']['3h']
                date = x['list'][i]['dt_txt']
                z.append(tem)
                d.append(date)
            except Exception as e:
                z.append(0)
                date = x['list'][i]['dt_txt']
                d.append(date)
                pass
        print(z, d)
        trace1 = go.Scatter(x=d, y=z, marker={'color': 'blue', 'symbol': 104, 'size': "10"},
                            mode="lines", name='1st Trace')
        data = go.Data([trace1])
        layout = go.Layout(title=str(c_name + ' rainfall '), xaxis={'title': 'Time'}, yaxis={'title': 'rainfall (mm)'})
        figure = go.Figure(data=data, layout=layout)
        div2 = opy.plot(figure, auto_open=False, output_type='div')
        context['graph2'] = div2
        return context


def simple(request):
    return render(request, 'search.html')
