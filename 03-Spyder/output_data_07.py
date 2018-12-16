#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 09:27:16 2018

@author: ernesteins
"""

import pandas as pd
import numpy as np
import sqlite3

# a SQL
data_frame_guardado = pd.read_pickle('/home/ernesteins/Documents/Python/yaselga-moreira-ernesto-daniel/03-Spyder/artwork_data_fame.pickle')
seccion_df= data_frame_guardado.iloc[49980:50019,:].copy()
seccion2_df= data_frame_guardado.iloc[50020:50100,:].copy()

with sqlite3.connect(
        '/home/ernesteins/Documents/Python/yaselga-moreira-ernesto-daniel/03-Spyder/mi_base_de_datos.db'
        )as conexion:
    seccion_df.to_sql('Tate',conexion)
    
seccion2_df.to_sql(
        'Artwork',
        conexion, 
        if_exists = 'append'
        )

# a JSON    
seccion_df.to_json('/home/ernesteins/Documents/Python/yaselga-moreira-ernesto-daniel/03-Spyder/default.json')
seccion_df.to_json('/home/ernesteins/Documents/Python/yaselga-moreira-ernesto-daniel/03-Spyder/artwork.json',orient = 'table')

# a EXCEL
seccion_df.to_excel('/home/ernesteins/Documents/Python/yaselga-moreira-ernesto-daniel/03-Spyder/basico.xlsx',index = False)
seccion_df.to_excel('/home/ernesteins/Documents/Python/yaselga-moreira-ernesto-daniel/03-Spyder/basico.xlsx',
                    columns=[
                            "artist",
                            "title",
                            "year"])

# a EXCEL en varias hojas de trabajo
writer = pd.ExcelWriter('/home/ernesteins/Documents/Python/yaselga-moreira-ernesto-daniel/03-Spyder/multiples_hojas.xlsx'
                        ,engine='xlsxwriter')

seccion_df.to_excel(
        writer,
        sheet_name = "Preview",
        index = False)

data_frame_guardado.to_excel(
        writer,
        sheet_name = "Complete",
        index = False)
writer.save()

# Formateo condicional

artistas_contados=data_frame_guardado[
        'artist'].value_counts()

artistas_contados.head()
writer = pd.ExcelWriter('/home/ernesteins/Documents/Python/yaselga-moreira-ernesto-daniel/03-Spyder/colores.xlsx',
                        engine='xlsxwriter')
artistas_contados.to_excel(writer,sheet_name="Artist Counts")

hoja = writer.sheets['Artist Counts']

cell_range = 'B2:B{}'.format(len(artistas_contados.index))

formato = {
        'type':'2_color_scale',
        'min_value':'10',
        'min_type':'percentile',
        'max_value':'99',
        'max_type':'percentile'}

hoja.conditional_format(cell_range,formato)
writer.save()