from djgeojson.fields import PolygonField
from django.db import models
from django.contrib.gis.db import models as gismodels


class MushroomSpot(models.Model):

    title = models.CharField(max_length=256)
    id1=models.IntegerField(primary_key=True)
    
    geom = gismodels.PointField()
    objects = gismodels.GeoManager()
    def __unicode__(self):
        return self.title

