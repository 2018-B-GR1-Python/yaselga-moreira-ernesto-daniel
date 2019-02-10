import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json

df = pd.DataFrame
df = pd.read_json("/home/ernesteins/Documentos/python/yaselga-moreira-ernesto-daniel/proyectoFinal/BtcHw/recolectado/BtcRegistros.json")

# Limitamos el rango a los años 2017/01 - 2018/12

df20162018 = df[df['date'] <= '2019-01-01']
df20162018 = df20162018['2017-01-01' <= df20162018['date']]

plt.plot(df20162018['date'],df20162018['high'],
         df20162018['date'],df20162018['low'])

# Limitamos el rngo a la épica más caótica del bit coin 
# la cual fue entre Noviembre de 2017 y mayo de 2018

dfjunaug=df20162018[df20162018['date']<='2018-05-01']
dfjunaug=dfjunaug['2017-11-01' <= dfjunaug['date']]

plt.plot(dfjunaug['date'],dfjunaug['high'],
         dfjunaug['date'],dfjunaug['low'])

with open('/home/ernesteins/Documentos/python/yaselga-moreira-ernesto-daniel/proyectoFinal/tweets_ECUADOR_amd.json') as f:
   data = json.load(f)
print (data)

print pd.DataFrame(data)

dfEcuadorNvidia = pd.read_json('/home/ernesteins/Documentos/python/yaselga-moreira-ernesto-daniel/proyectoFinal/tweets_ECUADOR_amd.json',lines = True)
df2 = pd.read_json('/home/ernesteins/Documentos/python/yaselga-moreira-ernesto-daniel/proyectoFinal/tweets_ECUADOR_amd.json',lines=True)