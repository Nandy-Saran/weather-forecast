import pandas as pd

from datamodel.models import Crop

df = pd.read_csv('csv/CropsNew-Sheet.csv', sep=',', encoding='utf-8')
for row in df.itertuples():
    a = Crop.objects.create(name=row.Crop, seas_no=row.Season_num, MintempC=row.Min_TempC, MaxtempC=row.Max_TempC,
                            fertilizer=row.FertilizerKgpha, growthRegul=row.Growth_regulator,
                            pick_start=row.Picking_start, max_RainMM=row.max_Rain, min_RainMM=row.min_Rain,
                            min_yieldT=row.min_Yield, max_yieldT=row.max_Yield, pH_min=row.min_pH, pH_max=row.max_pH,
                            ferAdv=row.FertilizerAdv, irrAdv=row.IRRIGATIONMETHODS)
    print(a)
