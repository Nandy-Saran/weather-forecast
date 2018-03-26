import datetime

import plotly.graph_objs as go
import plotly.offline as opy
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


def prediction_mape(city='Coimbatore'):
    import numpy as np
    import pandas as pd
    from sklearn.tree import DecisionTreeRegressor

    df = pd.read_csv('districtwise1901_to_2002.csv')
    df.info()
    df.dropna(how='any', inplace=True)
    subdivs = df['District'].unique()
    num_of_subdivs = subdivs.size
    print('Total # of Subdivs: ' + str(num_of_subdivs))
    months = df.columns[3:15]
    df1 = df[df['District'] == 'Coimbatore']
    z = []
    df2 = df1[['Year', months[0], 'A']]
    x = {1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L'}
    z.append(df2)
    df2.columns = np.array(['Year', 'x4', 'mon'])

    for i in range(1, 12):
        df3 = df1[['Year', months[i], x[i]]]
        df3.columns = np.array(['Year', 'x4', 'mon'])
        df2.append(df3)
        z.append(df3)
    # print(df2.head(5))
    df2.index = range(df2.shape[0])
    df2 = pd.concat(z)

    dft = pd.read_csv('test.csv')
    newdf = dft.merge(df2, left_on=['Year', 'mon'], right_on=['Year', 'mon'])
    newdf.head()

    dft = pd.read_csv('test.csv')
    newdf = dft.merge(df2, left_on=['Year', 'mon'], right_on=['Year', 'mon'])
    newdf.head()

    newdf['summ'] = newdf['Year'] + (newdf['mon'] * 0.08333)
    newdf.head()

    df_train1 = newdf[(newdf['Year'] != 2002)]
    df_test1 = newdf[(newdf['Year'] == 2002)]

    df_train = df_train1[['Year', 'month', 'x4']]
    df_train.columns = np.array(['Year', 'month', 'y'])
    df_train.head()

    df_test = df_test1[['Year', 'month', 'x4']]
    df_test.columns = np.array(['Year', 'month', 'y'])
    df_test.head()

    reg = DecisionTreeRegressor(max_depth=20)
    reg.fit(df_train.drop('y', axis=1), df_train['y'])
    predicted_values = reg.predict(df_test.drop('y', axis=1))

    context = {}
    context['city'] = city

    residuals = predicted_values - df_test['y'].values
    residuals = residuals / df_test['y'].values
    residuals = np.abs(residuals)
    mape = np.mean(residuals) * 100
    print(residuals)
    print('mape : ' + str(mape) + '%')
    context['mape'] = mape

    datelist = df_test1['date'].values.tolist()
    import datetime

    date_objects = [datetime.datetime.strptime(date, '%Y/%m/%d').date() for date in datelist]

    y_pred = predicted_values
    y_actual = df_test['y'].values
    context['x'] = date_objects
    context['y_pred'] = y_pred
    context['y_act'] = y_actual

    return context


def prophet_prediction(city='Coimbatore'):
    from fbprophet import Prophet
    import numpy as np
    import pandas as pd

    # from subprocess import check_output
    df = pd.read_csv('districtwise1901_to_2002.csv')
    print(df.info())
    context = {}
    context['city'] = city
    df.dropna(how='any', inplace=True)
    subdivs = df['District'].unique()
    num_of_subdivs = subdivs.size
    print('Total # of Subdivs: ' + str(num_of_subdivs))
    print(subdivs)
    months = df.columns[3:15]
    df1 = df[df['District'] == 'Coimbatore']
    z = []
    df2 = df1[['Year', months[0], 'A']]
    x = {1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L'}
    z.append(df2)
    df2.columns = np.array(['Year', 'x4', 'mon'])

    for i in range(1, 12):
        df3 = df1[['Year', months[i], x[i]]]
        df3.columns = np.array(['Year', 'x4', 'mon'])
        df2.append(df3)
        z.append(df3)

    df2.index = range(df2.shape[0])
    df2 = pd.concat(z)

    dft = pd.read_csv('test.csv')
    newdf = dft.merge(df2, left_on=['Year', 'mon'], right_on=['Year', 'mon'])

    df_train1 = newdf[(newdf['Year'] != 2002)]
    df_test1 = newdf[(newdf['Year'] == 2002)]

    df_train = df_train1[['date', 'x4']]
    df_train.columns = np.array(['ds', 'y'])

    df_test = df_test1[['date', 'x4']]
    df_test.columns = np.array(['ds', 'y'])
    datelist = df_test['ds'].values.tolist()
    date_objects = [datetime.datetime.strptime(date, '%Y/%m/%d').date() for date in datelist]
    context['actual_val'] = df_test['y'].values
    context['date'] = date_objects

    m = Prophet()
    m.fit(df_train)

    predicted_values = m.predict(df_test.drop('y', axis=1))

    residuals = predicted_values['yhat'].values - df_test['y'].values
    context['predicted_val'] = predicted_values['yhat'].values
    context['predicted_val_upper'] = predicted_values['yhat_upper'].values

    residuals = residuals / df_test['y'].values
    residuals = np.abs(residuals)
    mape = np.mean(residuals) * 100
    context['mape'] = mape

    print(residuals)
    print('mape : ' + str(mape) + '%')

    print(predicted_values)
    return context


class Graph2(TemplateView):
    template_name = 'graph_proph.html'

    def get_context_data(self, **kwargs):
        xy = prophet_prediction()
        context = super(Graph2, self).get_context_data(**kwargs)
        x = xy['date']
        y_act = xy['actual_val']
        y_predict = xy['predicted_val']
        y_upper = xy['predicted_val_upper']

        c_name = xy['city']
        context['mape'] = xy['mape']
        trace1 = go.Scatter(x=x, y=y_act, marker={'color': 'blue', 'symbol': 104, 'size': "50"},
                            mode="lines", name='Actual Rainfall')
        trace2 = go.Scatter(x=x, y=y_predict, marker={'color': 'green', 'symbol': 104, 'size': "50"},
                            mode="lines", name='Predicted Rainfall')
        trace3 = go.Scatter(x=x, y=y_upper, marker={'color': 'red', 'symbol': 104, 'size': "50"},
                            mode="lines", name='Predicted Rainfall Upper Bound')
        data = go.Data([trace1, trace2, trace3])
        layout = go.Layout(title=str(c_name + ' Rainfall'), xaxis={'title': 'date'}, yaxis={'title': 'Rainfall'})
        figure = go.Figure(data=data, layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div')
        context['graph'] = div

        return context


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


class Graph_mape(TemplateView):
    template_name = 'graph_proph.html'

    def get_context_data(self, **kwargs):
        xy = prediction_mape()
        context = super(Graph_mape, self).get_context_data(**kwargs)
        x = xy['x']
        y_act = xy['y_act']
        y_predict = xy['y_pred']

        c_name = xy['city']
        context['mape'] = xy['mape']
        trace1 = go.Scatter(x=x, y=y_act, marker={'color': 'blue', 'symbol': 104, 'size': "50"},
                            mode="lines", name='Actual Rainfall')
        trace2 = go.Scatter(x=x, y=y_predict, marker={'color': 'green', 'symbol': 104, 'size': "50"},
                            mode="lines", name='Predicted Rainfall')
        # trace3 = go.Scatter(x=x, y=y_upper, marker={'color': 'red', 'symbol': 104, 'size': "50"},
        #                     mode="lines", name='Predicted Rainfall Upper Bound')
        data = go.Data([trace1, trace2])
        layout = go.Layout(title=str(c_name + ' Rainfall'), xaxis={'title': 'date'}, yaxis={'title': 'Rainfall'})
        figure = go.Figure(data=data, layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div')
        context['graph'] = div

        return context
