# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import pandas as pd

df = pd.DataFrame

df = pd.read_json("/home/ernesteins/Documentos/python/yaselga-moreira-ernesto-daniel/proyectoFinal/BtcHw/recolectado/BtcRegistros.json")

df1 = df

df1 = df1.set_index('date')

