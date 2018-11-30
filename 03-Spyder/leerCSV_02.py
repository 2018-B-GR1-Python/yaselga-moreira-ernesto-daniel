#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 09:56:42 2018

@author: ernesteins
"""

import pandas as pd
import os

CSV_PATH = "/home/ernesteins/Documents/Introduccion-al-desarrollo-web/yaselga-moreira-ernesto-daniel/03-Spyder/artwork_data.csv"

# archivos que puede leer panda
# 1)archivos de texto -> CSV, JSON, HTML
# 2)archivos binarios
# 3)Bases de datos relacionales

data_frame_artwok = pd.read_csv(CSV_PATH, nrows=5, index_col = "id", usecols = ['id','artist'])

columnas_a_utilizar = ['id','artist','title',
                       'medium','year',
                       'acquisitionYear',
                       'height','width',
                       'units']

data_frame_artwok_completo = pd.read_csv(CSV_PATH
                                         ,index_col = 'id'
                                         ,usecols = columnas_a_utilizar)
data_frame_artwok_completo.shape

# -->Serializacion del DataFrame
# -->Deserializacion del DataFrame
# 1,2,4,6,7,4,6,9,0,1,2 --> Dataframe = BINARIO
# BINARIO -> DataFrame

PATH_FUARDADO = "/home/ernesteins/Documents/Introduccion-al-desarrollo-web/yaselga-moreira-ernesto-daniel/03-Spyder/artwork_data_fame.pickle"
data_frame_artwok_completo.to_pickle(PATH_FUARDADO)

df_completo_pickle = pd.read_pickle(PATH_FUARDADO)
