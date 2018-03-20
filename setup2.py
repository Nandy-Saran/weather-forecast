import csv
from django.contrib.gis.geos import Point

from mushrooms.models import MushroomSpot


csv_file = 'mycsv.csv'

def dms2dec(value):
    """
    Degres Minutes Seconds to Decimal degres
    """
    degres, minutes, seconds = value.split()
    #seconds, direction = seconds[:-1], seconds[-1]
    dec = float(degres) + float(minutes)/60 + float(seconds)/3600
    #if direction in ('S', 'W'):
    #    return -dec
    return dec

reader = csv.DictReader(open(csv_file), delimiter=",")
for line in reader:
    lng = dms2dec(line.pop('mlong'))
    lat = dms2dec(line.pop('mlat'))
    wmoid = int(line.pop('id'))
    name = line.pop('place').title()
    print(lng,lat)
    MushroomSpot(id1=wmoid, title=name, geom=Point(lng, lat)).save()
