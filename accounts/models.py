from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from datamodel.models import Crop, Place


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)


class Subscriber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    Mobile_no = models.CharField(max_length=15)
    land_ha = models.FloatField(max_length=15, blank=True, null=True)
    soil_type = models.CharField(max_length=15, blank=True, null=True)
    soil_ph = models.FloatField(max_length=10, blank=True, null=True)
    district = models.CharField(max_length=10, blank=True, null=True)
    location = models.ForeignKey(Place)
    category = models.CharField(max_length=25, blank=True, null=True)
    yield_tons = models.FloatField(null=True)
    datOfSow=models.DateField(null=True,blank=True)
    currentCrop = models.ForeignKey(Crop, related_name='crop_2_name', blank=True, null=True)
    prevCrop = models.ForeignKey(Crop, related_name='crop_1_Name', blank=True, null=True)
    pHadv=models.CharField(max_length=150)
    picMsg=models.CharField(max_length=150)
    cropmes=models.CharField(max_length=180)
    recCrop=models.CharField(max_length=260)
    ElecConduc = models.FloatField(blank=True, null=True)
    OrgCarbonP = models.FloatField(blank=True, null=True)
    Nitrogenkgha = models.FloatField(blank=True, null=True)
    Phosphoruskgha = models.FloatField(blank=True, null=True)
    Potassium_kgha = models.FloatField(blank=True, null=True)
    Sulphur_ppm = models.FloatField(blank=True, null=True)
    Zinc_ppm = models.FloatField(blank=True, null=True)
    Boron_ppm = models.FloatField(blank=True, null=True)
    Ironppm = models.FloatField(blank=True, null=True)
    Manganese_ppm = models.FloatField(blank=True, null=True)
    Copper_ppm = models.FloatField(blank=True, null=True)
    Waterph = models.FloatField(blank=True, null=True)
    min2months = models.FloatField(blank=True, null=True)
    max2months = models.FloatField(blank=True, null=True)
    isCurFarm=models.BooleanField(default=False)


class sms_farmer(models.Model):
    farmer = models.ForeignKey(Subscriber)
    crop = models.ForeignKey(Crop)






@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
