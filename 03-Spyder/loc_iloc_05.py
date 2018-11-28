#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 10:01:55 2018

@author: ernesteins
"""

import pandas as pd
import os

df = pd.read_pickle('/home/ernesteins/Documents/Introduccion-al-desarrollo-web/yaselga-moreira-ernesto-daniel/03-Spyder/artwork_data_fame.pickle')

df.loc[1035,'artist']

# df.loc[0,0] # Error

df.iloc[0,1]

df.iloc[0,:]

df.iloc[0:2,0:2]

df['height']
df['width']
#df['height'] * df['width']
df_width = df['width']
dfsort_values = df['width'].sort_values()
dfsort_values_head = df['width'].sort_values().head(100)
dfsort_values_tail = df['width'].sort_values().tail(100)

# convierte a numerico una serie 
pd.to_numeric(df['width'])
# errors = 'coerce' covierte en NaN los strings que no puede convertir en numero
a = pd.to_numeric(df['width'], errors='coerce')
b = pd.to_numeric(df['height'], errors='coerce')

#loc indice basado en la columna
#iloc indice basado en 0

df.loc[:,'width'] = a
df.iloc[:,6] = b


area = df['height'] * df['width']

type(area)

# assign agrega nuevas columna(serie) al dataframe
df = df.assign(area = area)

#dfarea = df['area'].sort_values().

dfarea = df['area'].max()

id_max_area = df['area'].idxmax()
id_min_area = df['area'].idxmin()

mayor_area = df.loc[id_max_area,:]
menor_area = df.loc[id_min_area,:]

# append añade nueva fila al dataframe (si tiene más columnas se agrega esa en todo el dataframe)

# Agregar una nueva serie al Dataframe
# 1) Definir los datos como arreglo

nuevo= ['10','Ernesto','mangos al amanecer', 
        'Graphite on paper','2015','2017', 
        '200','300','mm','600']
# 2) Definir las columnas
indices = list(df) # list(df) no devuelve el index
indices.insert(0,'index') #insertamos el index

# 3) Definir la serie
serie_nuevo = pd.Series(nuevo,index= indices)
serieN = serie_nuevo.transpose()

# 4) Creamos un df con las nuevas columnas y la transponemos
df_aux = pd.DataFrame(serie_nuevo).transpose()

df2 = df

df2.append(serieN, ignore_index = True)

Ernsto_artist = df["artist"] == "Ernesto"

Ernsto_artist.value_counts()
