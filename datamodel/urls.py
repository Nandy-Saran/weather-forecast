from django.conf.urls import url, include
from datamodel.views import crop_advices, start

urlpatterns = [
    url(r'^$', start, name="start"),
    url(r'^crop_advices/$', crop_advices, name="crop_advices")]
