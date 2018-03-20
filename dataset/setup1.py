import pandas as pd
from dataset.models import pincode
df=pd.read_csv('pincode1.csv',encoding='utf8',sep=',')
count = 0
for row in df.itertuples():
    print(count)
    count = count +1 
    obj=pincode.objects.create(pinc=row.pincode,place=row.taluk,district=row.districtname,state=row.statename,region=row.regionname,division=row.divisionname)

