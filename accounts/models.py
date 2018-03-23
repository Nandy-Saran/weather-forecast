from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)


class Subsciber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    Mobile_no = models.CharField(max_length=15)
    land_ha = models.FloatField(max_length=15, blank=True, null=True)
    soil_type = models.CharField(max_length=15, blank=True, null=True)
    soil_ph = models.FloatField(max_length=10, blank=True, null=True)
    district = models.CharField(max_length=10, blank=True, null=True)
    sub_district = models.CharField(max_length=10, blank=True, null=True)
    category = models.CharField(max_length=10, blank=True, null=True)
    yield_tons = models.FloatField(null=True)
    crop1 = models.CharField(max_length=30, blank=True, null=True)
    crop2 = models.CharField(max_length=30, blank=True, null=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()