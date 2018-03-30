from datamodel.models import Place,State
import pandas as pd

df=pd.read_csv('csv/Indian-States-and-Districts-List.csv',sep=',',encoding='utf-8')

lis1=df['State'].unique()
for i in lis1:
    StatCreat=State.objects.create(name=i)

for i in df.itertuples():
    print(i.State,i.District)
    StatInst=State.objects.get(name=i.State)
    PlacCreat=Place.objects.create(name=i.District,state=StatInst)


#a = ['Coimbatore', 'Chennai', 'pondicherry', 'madurai', 'mannargudi', 'cuddalore', 'villupuram', 'shillong', 'mathura',
#     'delhi', 'cherrapunji', 'thiruvananthapuram']
#for i in a:
#    s = Place.objects.create(name=i)
