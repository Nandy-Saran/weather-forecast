from django.conf.urls import url, include
from datamodel.views import index, start

urlpatterns = [
    url(r'^$', start, name="start"),
    url(r'^index$', index, name="index")]
