# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 12:43:49 2021

@author: Gabriel Macias
"""

import pandas as pd
import numpy as np


url = "Casos_positivos_de_COVID-19_en_Colombia.csv"
df = pd.read_csv(url)

df.drop(['Pertenencia étnica', 'Nombre del grupo étnico', 'Nombre del país',
         'Código ISO del país', 'Tipo de recuperación'], axis=1, inplace=True)

df.loc[df['Ubicación del caso'] ==
       'CASA', 'Ubicación del caso'] = 'Casa'

df.loc[df['Ubicación del caso'] ==
       'casa', 'Ubicación del caso'] = 'Casa'

df.loc[df['Estado'] == 'leve', 'Estado'] = 'Leve'

df.loc[df['Estado'] == 'LEVE', 'Estado'] = 'Leve'

df.loc[df['Recuperado'] == 'fallecido'] = 'Fallecido'

df.loc[df['Tipo de contagio'] == 'En Estudio'] = 'En estudio'

df.loc[df['Tipo de contagio'] == 'Comunitario'] = 'Comunitaria'

df.loc[df['Sexo'] == 'm'] = 'M'

df.loc[df['Sexo'] == 'f'] = 'F'

# 1. Número de casos de Contagiados en el País.

df['Estado'].size

# 2. Número de Municipios Afectados

df['Nombre municipio'].value_counts().shape

# 3. Liste los municipios afectados (sin repetirlos)

df['Nombre municipio'].value_counts()

# 4. Número de personas que se encuentran en atención en casa

casa = df[df['Ubicación del caso'] == 'Casa']
casa['Ubicación del caso'].value_counts()

# 5. Número de personas que se encuentran recuperados

recuperado = df[df['Recuperado'] == 'Recuperado']
recuperado.Recuperado.value_counts()

# 6. Número de personas que ha fallecido

fallecido = df[df['Recuperado'] == 'Fallecido']
fallecido.Recuperado.value_counts()

# 7. Ordenar de Mayor a menor por tipo de caso (Importado, en estudio,
# Relacionado)

df['Tipo de contagio'].value_counts()

# 30. Liste de mayor a menor la cantidad de fallecidos por edad en toda
# Colombia.

fallecido.groupby(['Nombre departamento', 'Edad']).size().sort_values(ascending=False)

# 9. Liste los departamentos afectados(sin repetirlos)

df['Nombre departamento'].value_counts()

# 10. Ordene de mayor a menor por tipo de atención

df['Ubicación del caso'].value_counts()

# 11. Liste de mayor a menor los 10 departamentos con mas casos de
# contagiados

df['Nombre departamento'].value_counts().head(10)

# 12. Liste de mayor a menor los 10 departamentos con mas casos de
# fallecidos

fallecido.groupby(['Nombre departamento', 'Estado']).size().sort_values(ascending=False).head(10)

# 13. Liste de mayor a menor los 10 departamentos con mas casos de
# recuperados

recuperado.groupby(['Nombre departamento', 'Recuperado']).size().sort_values(ascending=False).head(10)

# 14. Liste de mayor a menor los 10 municipios con mas casos de
# contagiados

df['Nombre municipio'].value_counts().head(10)

# 15. Liste de mayor a menor los 10 municipios con mas casos de
# fallecidos

fallecido.groupby(['Nombre municipio', 'Estado']).size().sort_values(ascending=False).head(10)