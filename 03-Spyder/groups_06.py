#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 07:37:48 2018

@author: ernesteins
"""

import pandas as pd
import os
import numpy as np

data_frame_guardado = pd.read_pickle('/home/ernesteins/Documents/Python/yaselga-moreira-ernesto-daniel/03-Spyder/artwork_data_fame.pickle')

seccion_data_frame = data_frame_guardado.iloc[49980:50019,:].copy()

sdf_agrupado = seccion_data_frame.groupby('artist')

type(sdf_agrupado)

for name, group_fd in sdf_agrupado:
  print(name)
  print(group_fd)
  break


# Agregacion Minimo
for name, group_fd in sdf_agrupado:
  anio_minimo = group_fd['acquisitionYear'].min()
  print("{}:{}").format(name,anio_minimo)

def llenar_valores_vacios(series):
    valores_contados = series.value_counts()
    if valores_contados.empty:
        return series
    
    print(valores_contados)
    valores_mas_utilizados = valores_contados.index[0]
    
    nuevo_valor = series.fillna(valores_mas_utilizados)
    
    
    
    return nuevo_valor

def transformar_df_por_artista(df):
    agrupado_por_artista = df.groupby('artist')
    
    for nombre_artista, grupo in agrupado_por_artista:
        df_llenado = grupo.copy()
        print(grupo['width'])
#        print(agrupado_por_artista)
        df_llenado.loc[:,'width']=llenar_valores_vacios(grupo['width'])
        
transformar_df_por_artista(seccion_data_frame)
