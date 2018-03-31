import pandas as pd
from datamodel.models import Crop
df = pd.read_csv('csv/CropsNew-Sheet2.csv', sep=',', encoding='utf-8')
for row in df.itertuples():
    #print('depends')
    print(row.Crop)
    a=Crop.objects.get(name=row.Crop)
    a.ElecConduc=row.ECdsm
    a.OrgCarbonP=row.OrganicCarbonP
    a.Nitrogenkgha=row.Nitrogenkgha
    a.Phosphoruskgha=row.Phosphoruskgha
    a.Potassium_kgha=row.Potassium_kgha
    a.Sulphur_ppm=row.Sulphur_ppm
    a.Zinc_ppm=row.Zinc_ppm
    a.Boron_ppm=row.Boron_ppm
    a.Ironppm=row.Ironppm
    a.Manganese_ppm=row.Manganese_ppm
    a.Copper_ppm=row.Copper_ppm
    a.Waterph=row.Waterph
    a.min2months=row.min2months
    a.max2months=row.max2months
    a.save()
    print(a.Boron_ppm)

