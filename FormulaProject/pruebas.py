#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 07:58:17 2018

@author: ernesteins
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# extracción de datos

path = "/home/ernesteins/Documents/Introduccion-al-desarrollo-web/yaselga-moreira-ernesto-daniel/FormulaProject/F1"

circuits =  pd.read_csv(path+'/circuits.csv',index_col="circuitId")
constructorResults =  pd.read_csv(path+'/constructorResults.csv',index_col="constructorResultsId")
constructors =  pd.read_csv(path+'/constructors.csv',index_col="constructorId")
constructorStandings =  pd.read_csv(path+'/constructorStandings.csv',index_col="constructorStandingsId")
drivers =  pd.read_csv(path+'/drivers.csv',index_col="driverId")
driverStandings =  pd.read_csv(path+'/driverStandings.csv',index_col="driverStandingsId")
lapTimes =  pd.read_csv(path+'/lapTimes.csv',index_col="raceId")
pitStops =  pd.read_csv(path+'/pitStops.csv',index_col="raceId")
qualifying =  pd.read_csv(path+'/qualifying.csv',index_col="qualifyId")
races =  pd.read_csv(path+'/races.csv',index_col="raceId")
results =  pd.read_csv(path+'/results.csv',index_col="resultId")
seasons =  pd.read_csv(path+'/seasons.csv')
status =  pd.read_csv(path+'/status.csv',index_col="statusId")

## CUÁNTOS CIRCUITOS DE LA F1 HAN HABIDO A LO LARGO DE LOS TIEMPOS

print ("Han existido un total de: ",circuits["name"].size," circuitos a lo largo de la historia de la F1")
print (circuits["name"])

## CIRCUITOS POR PAIS

plt.title("Circuitos por Nacion"),
circuits['country'].value_counts().plot(kind='bar')
plt.show()

### HAN HABIDO MÁS PILOTOS DE NACIONES EUROPEAS

plt.title("Conductores por Nacion"),
drivers['nationality'].value_counts().plot(kind='bar')

## UN PAÍS EUROPEO HA TENIDO MÁS ESCUDERIAS

plt.title("Conductores por Nacion"),
constructors['nationality'].value_counts().plot(kind='bar')

## ANTES SE CORRÍAN MENOS CARRERAS POR AÑO

plt.title("Circuitos por año")
plt.bar(races['year'].unique(),
        races['year'].value_counts(False,False))
plt.show()

### PIT-STOP MÁS RAPIDOS POR CIRCUITO
races_pitStop = pd.concat([races, pitStops], axis=1, join_axes=[pitStops.index])
races_pitStop[['milliseconds',
               'name',
               'date']].sort_values(by = 'milliseconds').groupby('name').min()

## TOP 10 PIT-STOP MÁS RÁPIDOS

races_pitStop[['milliseconds',
               'name',
               'date']].sort_values(by = 'milliseconds').head(10)

### LOS CORREDORES DE LA ERA HÍBRIDA 
### TIENEN LAS VUELTAS MÁS RÁPIDAS
### POR EL DESARROLLO MODERNO DE LOS F1

laps_drivers = lapTimes.join(drivers,"driverId")
laps_drivers["milliseconds"] = laps_drivers["milliseconds"]/(1000*60)
laps_drivers.rename(columns={"milliseconds":"minutos"},inplace = True)

laps_drivers[["minutos","driverRef"]].sort_values(by = 'minutos').head(20)

### LA VUELTA MÁS RAPIDA (EN CARRERA) 
### SIEMPRE ES AL FINAL DE LA CARRERA

laps_drivers[["minutos","lap"]].sort_values(by = 'minutos').head(20)

### FERRARI ES LA ESCUDERÍA CON MÁS VICTORIAS
constructor_standing_completo = constructorStandings.join(constructors,"constructorId")
constructores_P1_bool = constructor_standing_completo["position"]==1
constructores_P1 =  constructor_standing_completo[constructores_P1_bool]
constructores_P1["name"].value_counts()

### EL CORREDOR MÁS JOVEN EN PISTA ES MAX VERSTAPPEN

drivers_dob = drivers["dob"]
drivers_dob = drivers_dob.str.split("/",expand = True)
drivers_dob.rename(columns={0:"dayob",1:"monthob",2:"yearob"},inplace = True)
drivers_dob = drivers.join(drivers_dob,"driverId")

drivers_dob["yearob"] = drivers_dob["yearob"].fillna(0).astype(object).astype(int)
2018 - drivers_dob["yearob"].max()

drivers_dob[].loc[drivers_dob["yearob"]==drivers_dob["yearob"].max()]

drivers_dob[["driverRef",
                  "number",
                  "code",
                  "forename",
                  "surname",
                  "dob",
                  "nationality"]].loc[drivers_dob["yearob"]==drivers_dob["yearob"].max()]
