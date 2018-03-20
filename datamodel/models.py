from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=30)
    Lat=models.CharField(max_length=30,blank=True)
    Long=models.CharField(max_length=30,blank=True)
    Pincode=models.CharField(max_length=30,blank=True)


class Weather(models.Model):
    place=models.ForeignKey(Place)
    date=models.CharField(max_length=30)
    datenum=models.CharField(max_length=30)
    moonrise=models.CharField(max_length=30)
    moonset=models.CharField(max_length=30)
    sunrise=models.CharField(max_length=30)
    sunset=models.CharField(max_length=30)
    maxtempC=models.CharField(max_length=30)
    mintempC=models.CharField(max_length=30)
    rainMM=models.CharField(max_length=30)
    pressure=models.CharField(max_length=30)
    humidity=models.CharField(max_length=30)
    WindSpeedMil=models.CharField(max_length=30)
    WindGustMil=models.CharField(max_length=30)
    Winddir16Point=models.CharField(max_length=30)
    WindDesc=models.CharField(max_length=100,default='')
    WindDirdeg=models.CharField(max_length=30,default='')



class Crop(models.Model):
    name=models.CharField(max_length=30)
    seas_no=models.CharField(max_length=30)
    MintempC=models.CharField(max_length=30,blank=True)
    MaxtempC=models.CharField(max_length=30,blank=True)
    fertilizer=models.CharField(max_length=150,blank=True)
    growthRegul=models.CharField(max_length=230,blank=True)
    pick_start=models.CharField(max_length=30,blank=True)
    count=models.CharField(max_length=30,blank=True)
    interv=models.CharField(max_length=30,blank=True)
    yieldT=models.CharField(max_length=30,blank=True)
    FlowIniti=models.CharField(max_length=50,blank=True)


