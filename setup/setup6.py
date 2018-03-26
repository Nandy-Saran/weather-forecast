import pandas as pd

from datamodel.models import Pest, Crop, Pesticide

df1 = pd.read_csv('Pests-Sheet1.csv', sep=',')
df2 = pd.read_csv('Pesticides-Sheet1.csv', sep=',')
for inst in df2.itertuples():
    try:
        s = Pesticide.objects.create(pestname=inst.PESTS.strip(), pesticide=inst.PESTICIDES.strip())
        print(s.pestname)
    except:
        print('NO')
for inst in df1.itertuples():
    ins = Crop.objects.get(name=inst.CROPS)
    print(inst.CROPS)
    ar = inst.PEST.split(',')
    tot = []
    a = Pest.objects.create(crop=ins)
    print(ins.pk)
    for i in ar:
        tem = Pesticide.objects.get(pestname=i.strip())
        print(tem.pestname)
        a.pest.add(tem)
        print(a.pest.all())
    print('ok')
    a.save()
