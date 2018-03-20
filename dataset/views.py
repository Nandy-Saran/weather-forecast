import pandas as pd
from dataset.models import pincode
df=pd.read_csv('pincode1.csv',encoding='utf8',sep=',')
lis=['pincode','taluk']
df1=df[lis]
for row in df1.itertuples:
    row=pincode.objects.create(pinc=row.pincode,place=row.taluk)
