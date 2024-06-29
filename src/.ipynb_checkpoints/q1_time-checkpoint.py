from typing import List, Tuple
from datetime import datetime
import time
import pandas as pd
import json
import os
import re
import memory_profiler

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Identifica las 10 fechas con más tweets y el usuario más frecuente para cada una de esas fechas.
    Leer el archivo línea por línea y devuelve una lista de tuplas con las fechas y los usuarios más frecuentes.
    
    Returns:
    List[Tuple[datetime.date, str]]: Lista de tuplas, cada una con una fecha y el usuario más frecuente en esa fecha.
    """
    # Leer el archivo línea por línea
    tweets = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            tweets.append(json.loads(line.strip()))

    # Convertir la lista de tweets a un DataFrame de pandas
    df = pd.DataFrame(tweets)

    # Convertir la columna 'date' a objeto de fecha y extraer solo la fecha (sin la hora)
    df['date'] = pd.to_datetime(df['date']).dt.date
    
    # Contar la frecuencia de cada fecha y seleccionar las 10 fechas con más tweets
    top_dates = df['date'].value_counts().nlargest(10).index
    
    # Inicializar una lista para almacenar los resultados
    result = []
    
    # Para cada fecha en las 10 fechas más frecuentes

    
    # Para cada fecha en las 10 fechas más frecuentes
    for i in top_dates:
        # Filtrar el DataFrame para obtener solo las filas con la fecha actual
        fecha_i = df[df['date'] == i]
        
        # Obtener la columna 'user' de las filas filtradas
        top_users = fecha_i['user']
        
        # Encontrar el usuario más frecuente en esa fecha
        top_users_fr = top_users.mode()
        
        # Obtener el primer valor del modo (que es el usuario más frecuente)
        top_user_fr = top_users_fr.values[0]
        
        # Obtener el nombre de usuario del diccionario 'user'
        top_user_fr_username = top_user_fr['username']
        
        # Añadir la fecha y el usuario a la lista de resultados
        result.append((str(i), top_user_fr_username))
    
    
    return result