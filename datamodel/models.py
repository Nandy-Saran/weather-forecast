from django.db import models


# Create your models here.

class State(models.Model):
    name=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=30)
    Lat = models.CharField(max_length=30, blank=True)
    Long = models.CharField(max_length=30, blank=True)
    Pincode = models.CharField(max_length=30, blank=True)
    state=models.ForeignKey(State)
    cropList=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name



class Weather(models.Model):
    place = models.ForeignKey(Place)
    date = models.DateField(max_length=30)
    datenum = models.IntegerField()
    moonrise = models.CharField(max_length=30)
    moonset = models.CharField(max_length=30)
    sunrise = models.CharField(max_length=30)
    sunset = models.CharField(max_length=30)
    maxtempC = models.FloatField()
    mintempC = models.FloatField()
    rainMM = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    WindSpeedMil = models.FloatField()
    WindGustMil = models.FloatField()
    Winddir16Point = models.CharField(max_length=30)
    WindDesc = models.CharField(max_length=100)
    WindDirdeg = models.IntegerField()

    def __str__(self):
        return self.place.name


class Crop(models.Model):
    name = models.CharField(max_length=30)
    seas_no = models.CharField(max_length=50, blank=True, null=True)
    pH_min = models.FloatField(blank=True, null=True)
    pH_max = models.FloatField(blank=True, null=True)
    min_yieldT = models.FloatField(blank=True, null=True)
    MintempC = models.FloatField(blank=True, null=True)
    MaxtempC = models.FloatField(blank=True, null=True)
    fertilizer = models.CharField(max_length=150, blank=True, null=True)
    growthRegul = models.CharField(max_length=230, blank=True, null=True)
    pick_start = models.FloatField(blank=True, null=True)
    count = models.FloatField(blank=True, null=True)
    interv = models.FloatField(blank=True, null=True)
    max_yieldT = models.FloatField(blank=True, null=True)
    FlowIniti = models.FloatField(blank=True, null=True)
    min_RainMM = models.FloatField(blank=True, null=True)
    max_RainMM = models.FloatField(blank=True, null=True)
    #pests = models.CharField(max_length=150, blank=True, null=True)
    ferAdv=models.CharField(max_length=300,null=True,blank=True)
    irrAdv=models.CharField(max_length=300,null=True,blank=True)
    ElecConduc=models.FloatField(blank=True,null=True)
    OrgCarbonP=models.FloatField(blank=True,null=True)
    Nitrogenkgha=models.FloatField(blank=True,null=True)
    Phosphoruskgha=models.FloatField(blank=True,null=True)
    Potassium_kgha=models.FloatField(blank=True,null=True)
    Sulphur_ppm=models.FloatField(blank=True,null=True)
    Zinc_ppm=models.FloatField(blank=True,null=True)
    Boron_ppm=models.FloatField(blank=True,null=True)
    Ironppm=models.FloatField(blank=True,null=True)
    Manganese_ppm=models.FloatField(blank=True,null=True)
    Copper_ppm=models.FloatField(blank=True,null=True)
    Waterph=models.FloatField(blank=True,null=True)
    min2months=models.FloatField(blank=True,null=True)
    max2months=models.FloatField(blank=True,null=True)

    def __str__(self):
        return self.name


class Pesticide(models.Model):
    pestname = models.CharField(max_length=50)
    pesticide = models.CharField(max_length=300)

    def __str__(self):
        return self.pestname

class Disease(models.Model):
    diseaseName=models.CharField(max_length=50)
    Symptoms=models.TextField(blank=True,null=True)
    Remedy=models.TextField(blank=True,null=True)
    def __str__(self):
        return self.diseaseName

class disPest(models.Model):
    pest = models.ManyToManyField(Pesticide)
    crop = models.OneToOneField(Crop)
    disease=models.ManyToManyField(Disease)

    def __str__(self):
        return self.crop.name
'''
class crop1(models.Model):
    name=models.CharField(max_length=30)
    disease=models.ManyToManyField(Disease)


class Disease(models.Model):
    Disease=models.CharField(max_length=264)
    Symptoms=models.CharField(max_length=528)
'''

