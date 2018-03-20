from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    Mobile_no = models.CharField(max_length=15)
    land_ha = models.FloatField(max_length=15, blank=True)
    soil_type = models.CharField(max_length=15, blank=True)
    soil_ph = models.FloatField(max_length=10, blank=True)
    district = models.CharField(max_length=10, blank=True)
    sub_district = models.CharField(max_length=10, blank=True)
    category = models.CharField(max_length=10, blank=True)
    yield_tons = models.FloatField()
    crop1 = models.CharField(max_length=30, blank=True)
    crop2 = models.CharField(max_length=30, blank=True)
    email_confirmed = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()