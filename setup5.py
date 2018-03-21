from datamodel.models import Crop
import pandas as pd

df = pd.read_csv('Crops-Sheet1.csv', sep=',', encoding='utf-8')
for row in df.itertuples():
    a=Crop.objects.create(name=row.Crop,seas_no=row.Season_num,MintempC=row.Min_Temp(Celsius),MaxtempC=row.Max_Temp(Celsius),fertilizer=Fertilizer(Kg/ha),growthRegul=Growth_regulator,pick_start=Picking_start(days),count=row.Count,interv=row.Gap,yieldT=row.Yield,FlowIniti=row.Flower_Initiation)
    print(a)


