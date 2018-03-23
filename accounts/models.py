from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datamodel.models import Place,Crop


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Place)
    email_confirmed = models.BooleanField(default=False)
    mobile = models.CharField(max_length=20)
    land_ha=models.FloatField(blank=True)
    name=models.CharField(max_length=30,blank=True,null=True)
    soil_ph=models.FloatField(blank=True,null=True)
    soil_type=models.CharField(max_length=20,blank=True,null=True)
    district=models.CharField(max_length=25,blank=True,null=True)
    category=models.CharField(max_length=30,blank=True,null=True)
    crop1=models.ForeignKey(Crop,related_name='crop1_set')
    date_of_sow=models.DateField(blank=True,null=True)
    crop2=models.ForeignKey(Crop,related_name='crop2_set')
    yield_ton=models.FloatField(blank=True,null=True)
    aadhar=models.CharField(max_length=20,null=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
