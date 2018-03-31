from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

class crop(models.Model):
    Name = models.CharField(max_length=100)
    season = models.CharField(max_length=200)
    season_num = models.CharField(max_length=50)
    comments = models.CharField(max_length=200)
    min_temp = models.FloatField()
    max_temp = models.FloatField()
    fertilizer = models.CharField(max_length=50)
    flower_init = models.CharField(max_length=50)
    first_picking = models.CharField(max_length=100)
    growth_regulatore = models.TimeField()
    yield_crops = models.CharField(max_length=60)
    no_of_pickings = models.CharField(max_length=60)
    date_of_pickings = models.CharField(max_length=60)
    gap = models.IntegerField()
    Count = models.IntegerField()

    def __str__(self):
        return self.Name


class Crop_Disease(models.Model):
    Disease = models.CharField(max_length=264)
    Symptoms = models.CharField(max_length=528)
    Crops_Affected = models.CharField(max_length=264)
