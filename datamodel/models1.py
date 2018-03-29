from django.db import models

# Create your models here.
class Crop_Disease(models.Model):
    Disease=models.CharField(max_length=264)
    Symptoms=models.CharField(max_length=528)
    Crops_Affected=models.CharField(max_length=264)
