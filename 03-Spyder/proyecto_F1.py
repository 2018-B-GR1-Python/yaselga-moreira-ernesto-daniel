#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 14:53:00 2018

@author: ernesteins
"""

import numpy as np
import pandas as pd
path = "/home/ernesteins/Documents/formula-1-race-data-19502017/races.csv"
path_pilotos = "/home/ernesteins/Documents/formula-1-race-data-19502017/drivers.csv"
path_constructores = "/home/ernesteins/Documents/formula-1-race-data-19502017/constructors.csv"
path_constructores_results = "/home/ernesteins/Documents/formula-1-race-data-19502017/constructorResults.csv"

data_frame_constructores = pd.read_csv(path_constructores)
data_frame_constructores_results = pd.read_csv(path_constructores_results)

data_frame_races = pd.read_csv(path, index_col = 'raceId')
data_frame_drivers = pd.read_csv(path_pilotos)

data_frame_races['circuitId'].value_counts()
df_2000 = data_frame_races[data_frame_races["year"]==2000]

df_drivers_name = data_frame_drivers["driverRef"]
df_unique_drivers = pd.unique(df_drivers_name)

#número de pilotos que han corrido en la F1 desde 1950
len(df_unique_drivers)

