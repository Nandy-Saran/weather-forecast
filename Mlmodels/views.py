import datetime

import plotly.offline as opy
import plotly.graph_objs as go
from django.views.generic import TemplateView


def prediction(city='Coimbatore'):
    import numpy as np
    import pandas as pd
    from sklearn.tree import DecisionTreeRegressor
    df = pd.read_csv('districtwise1901_to_2002.csv')

    df.info()
    df.dropna(how='any', inplace=True)

    sub_divs = df['District'].unique()
    num_of_sub_divs = sub_divs.size
    print('Total # of Sub divs: ' + str(num_of_sub_divs))

    city = 'Coimbatore'
    months = df.columns[3:15]
    df1 = df[df['District'] == city]

    df2 = df1[['District', 'Year', months[0]]]
    df2.loc[:, 'mon'] = 0
    df2.columns = np.array(['District', 'Year', 'val', 'mon'])
    z = [df2]

    for i in range(1, 12):
        df3 = df1[['District', 'Year', months[i]]]
        df3['mon'] = i
        df3.columns = np.array(['District', 'Year', 'val', 'mon'])
        df2.append(df3)
        z.append(df3)
    df2.index = range(df2.shape[0])
    df2 = pd.concat(z)

    df2.drop('District', axis=1, inplace=True)
    msk = np.random.rand(len(df2)) < 0.8

    df_train = df2[msk]
    df_test = df2[~msk]
    df_train.index = range(df_train.shape[0])
    df_test.index = range(df_test.shape[0])

    reg = DecisionTreeRegressor(max_depth=20)

    dft = pd.read_csv('test.csv')
    dft.info()

    dft_test = dft[['Year', 'mon']]
    reg.fit(df2.drop('val', axis=1), df2['val'])
    predicted_values = reg.predict(dft_test)
    datelist = dft['date'].values.tolist()
    date_objects = [datetime.datetime.strptime(date, '%Y/%m/%d').date() for date in datelist]
    dic = {'x': date_objects, 'y': predicted_values, 'city': city}
    return dic


class Graph(TemplateView):
    template_name = 'graph.html'

    def get_context_data(self, **kwargs):
        xy = prediction()
        context = super(Graph, self).get_context_data(**kwargs)
        x = xy['x']
        y = xy['y']
        c_name = xy['city']

        trace1 = go.Scatter(x=x, y=y, marker={'color': 'red', 'symbol': 104, 'size': "50"},
                            mode="lines", name='1st Trace')
        data = go.Data([trace1])
        layout = go.Layout(title=str(c_name + ' Rainfall'), xaxis={'title': 'date'}, yaxis={'title': 'Rainfall'})
        figure = go.Figure(data=data, layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div')
        context['graph'] = div

        return context
