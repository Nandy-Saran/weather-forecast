from datamodel.models import Place, State
import pandas as pd
import numpy as np

for i in State.objects.all():
    i.delete()
df = pd.read_csv('csv/Indian-States-and-Districts-List.csv')
df.columns = np.array(['state', 'district', 'statetype', 'as', 'asd', 'asdd', 'cd'])

lis1 = df['state'].unique()
for i in lis1:
    obj = State.objects.create(name=i)
    print(obj)

for i in df.itertuples():
    print(i.state, i.district)
    StatInst = State.objects.get(name=i.state)
    place_obj = Place.objects.create(name=i.district, state=StatInst)

# a = ['Coimbatore', 'Chennai', 'pondicherry', 'madurai', 'mannargudi', 'cuddalore', 'villupuram', 'shillong', 'mathura',
#     'delhi', 'cherrapunji', 'thiruvananthapuram']
# for i in a:
#    s = Place.objects.create(name=i)
