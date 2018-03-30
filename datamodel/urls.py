from django.conf.urls import url, include
from datamodel.views import crop_advices, start,CalCropAr,fert_advices

urlpatterns = [
    url(r'^$', start, name="start"),
    url(r'^crop_advices/$', crop_advices, name="crop_advices"),
    url(r'^CalCropAr/$', CalCropAr, name='CalCropAr'),
    url(r'^fert_advices/$', fert_advices, name='fert_advices'),
    ]
