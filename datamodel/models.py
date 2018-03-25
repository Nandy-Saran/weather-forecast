from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=30)
    Lat=models.CharField(max_length=30,blank=True)
    Long=models.CharField(max_length=30,blank=True)
    Pincode=models.CharField(max_length=30,blank=True)

    def __str__(self):
        return self.name

class Weather(models.Model):
    place=models.ForeignKey(Place)
    date=models.DateField(max_length=30)
    datenum=models.IntegerField()
    moonrise=models.CharField(max_length=30)
    moonset=models.CharField(max_length=30)
    sunrise=models.CharField(max_length=30)
    sunset=models.CharField(max_length=30)
    maxtempC=models.FloatField()
    mintempC=models.FloatField()
    rainMM=models.FloatField()
    pressure=models.FloatField()
    humidity=models.FloatField()
    WindSpeedMil=models.FloatField()
    WindGustMil=models.FloatField()
    Winddir16Point=models.CharField(max_length=30)
    WindDesc=models.CharField(max_length=100)
    WindDirdeg=models.IntegerField()

    def __str__(self):
        return self.place.name



class Crop(models.Model):
    name=models.CharField(max_length=30)
    seas_no=models.CharField(max_length=50,blank=True,null=True)
    pH_min=models.FloatField(blank=True,null=True)
    pH_max=models.FloatField(blank=True,null=True)
    min_yieldT=models.FloatField(blank=True,null=True)
    MintempC=models.FloatField(blank=True,null=True)
    MaxtempC=models.FloatField(blank=True,null=True)
    fertilizer=models.CharField(max_length=150,blank=True,null=True)
    growthRegul=models.CharField(max_length=230,blank=True,null=True)
    pick_start=models.FloatField(blank=True,null=True)
    count=models.FloatField(blank=True,null=True)
    interv=models.FloatField(blank=True,null=True)
    max_yieldT=models.FloatField(blank=True,null=True)
    FlowIniti=models.FloatField(blank=True,null=True)
    min_RainMM=models.FloatField(blank=True,null=True)
    max_RainMM=models.FloatField(blank=True,null=True)
    pests=models.CharField(max_length=150,blank=True,null=True)

    def __str__(self):
        return self.name

class Pest(models.Model):
    name=models.CharField(max_length=50)
    crop=models.ForeignKey(Crop)
    
    def __str__(self):
        return self.name

class Pesticide(models.Model):   
    pest=models.ForeignKey(Pest)
    pesticide=models.CharField(max_length=300)