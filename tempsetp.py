#from datamodel.models import Place, Weather,State
import requests
import json
a=open('disease.json','r')
content=a.read()
print(content.json())
