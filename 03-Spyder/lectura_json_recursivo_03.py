#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 08:02:08 2018

@author: ernesteins
"""

import json
import pandas as pd
import os

directorio_leer = "/home/ernesteins/Documents/pandas-fundamentals/02/demos/demos/collection-master/artworks"

ejemplo_json= directorio_leer + "/a/000/a00001-1035.json"

llaves_a_usarse = ['id','all_artists','title','medium','dateText','height','width','units']

def obtener_registro_de_archivos_json(path_archivo, llaves):
    with open(path_archivo) as texto_json:
        contenido_json = json.load(texto_json)
    arreglo_valores_leidos = []
    for llave in llaves:
        arreglo_valores_leidos.append(contenido_json[llave])
    return tuple(arreglo_valores_leidos)
            
    
registro_json = obtener_registro_de_archivos_json(ejemplo_json,llaves_a_usarse)

registro_json_dt = pd.DataFrame([registro_json])

def leer_registros_json_en_carpetas(directorio, llaves):
    trabajos_arte_encontrados = []
    for path_raiz, lista_directorios, archivos in os.walk(directorio):
        for archivo in archivos:
            if archivo.endswith('json'):
                registro_encontrado = obtener_registro_de_archivos_json(
                        os.path.join(path_raiz,archivo), llaves)
                trabajos_arte_encontrados.append(registro_encontrado)
                break
    return pd.DataFrame.from_records(trabajos_arte_encontrados,columns = llaves, index = 'id')
        
df_artwoks = leer_registros_json_en_carpetas(directorio_leer,llaves_a_usarse)


    
