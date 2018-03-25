from django.db import models


# Create your models here.
class pincode(models.Model):
    pinc = models.CharField(max_length=6)
    place = models.CharField(max_length=25)
    division = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
