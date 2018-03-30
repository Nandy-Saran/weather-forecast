import pandas as pd
import numpy as np
from datamodel.models import Crop

df = pd.read_csv('csv/CropsNew-Sheet.csv', sep=',', encoding='utf-8')
df.columns = np.array(
    ['Crop', 'Season', 'min_Rain', 'max_Rain', 'Season_num', 'Min_TempC', 'Max_TempC', 'IRRIGATIONMETHODS',
     'FertilizerAdv',
     'FertilizerKgpha', 'Yield', 'min_Yield', 'max_Yield', 'Soil_pH', 'min_pH', 'max_pH',
     'Rainfall', '', '', 'Flower_Initiation', 'Ist_picking', 'Picking_start', 'Growth_regulator', 'No.of_pickings',
     'Date_of_pickings', 'Gap', 'Count'])

for row in df.itertuples():
    print(row)
    a = Crop.objects.create(name=row.Crop.strip(), seas_no=row.Season_num.strip(), MintempC=row.Min_TempC,
                            MaxtempC=row.Max_TempC,
                            fertilizer=row.FertilizerKgpha.strip(), growthRegul=row.Growth_regulator.strip(),
                            pick_start=row.Picking_start.strip(), max_RainMM=row.max_Rain, min_RainMM=row.min_Rain,
                            min_yieldT=row.min_Yield, max_yieldT=row.max_Yield.strip(), pH_min=row.min_pH,
                            pH_max=row.max_pH,
                            ferAdv=str(row.FertilizerAdv).strip(), irrAdv=str(row.IRRIGATIONMETHODS).strip())
    print(a)
