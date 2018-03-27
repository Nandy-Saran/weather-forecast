"""sms URL Configuration
"""
from django.conf.urls import url

from Mlmodels.views import Graph, Graph2, Graph_mape

urlpatterns = [

    url(r'^prediction/$', Graph.as_view(), name="prediction"),
    url(r'^prophet/$', Graph2.as_view(), name="prophet"),
    url(r'^mape/$', Graph_mape.as_view(), name="mape"),

]
