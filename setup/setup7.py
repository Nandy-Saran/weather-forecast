import pandas as pd

from datamodel.models import disPest, Crop, Pesticide,Disease

df1 = pd.read_csv('csv/Book11.csv',sep=',',encoding='utf-8')
df2 = pd.read_csv('csv/Book18.csv',sep=',',encoding='utf-8')
for inst in df2.itertuples():
    try:
        s = Disease.objects.create(diseaseName=inst.Disease.strip(),Symptoms=inst.Symptoms.strip(),Remedy=inst.Remedy.strip())
        print(s.diseaseName)
    except:
        print('NO')

for inst in df1.itertuples():
    try:
        ins = Crop.objects.get(name=inst.Crops.strip())
        print(inst.Crops)
        ar = inst.Diseases.split(',')
        tot = []
        a = disPest.objects.get(crop=ins)
        print(ins.pk)
        for i in ar:
            tem = Disease.objects.get(diseaseName=i.strip())
            tem = Disease.objects.get(diseaseName=i.strip())
            #print(tem.diseaseName)
            a.disease.add(tem)
        print(a.disease.all())
        #print('ok')
        a.save()
    except:
        print('No')
