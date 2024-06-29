from typing import List, Tuple
from datetime import datetime
import pandas as pd

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:

    """
    Procesa un archivo JSON en chunks para contar las fechas más frecuentes de tweets
    y determinar el usuario más activo en esas fechas.
    """
    # Inicializar diccionarios para contar fechas y usuarios
    date_counts = {}
    user_details = {}

    # Procesar el DataFrame en chunks para optimizar el uso de memoria
    for chunk in pd.read_json(file_path, lines=True, chunksize=10000):
        chunk['date'] = pd.to_datetime(chunk['date']).dt.date
        
        # Contar las fechas en el chunk
        for date in chunk['date'].unique():
            current_df = chunk[chunk['date'] == date]
            date_counts[date] = date_counts.get(date, 0) + len(current_df)
            
            # Contar usuarios para cada fecha
            if date not in user_details:
                user_details[date] = {}
            
            for user_dict in current_df['user']:
                # Asumiendo que cada 'user' es un diccionario que contiene un campo 'username'
                user = user_dict['username']
                if user in user_details[date]:
                    user_details[date][user] += 1
                else:
                    user_details[date][user] = 1

    # Determinar las 10 fechas más frecuentes
    top_dates = sorted(date_counts, key=date_counts.get, reverse=True)[:10]

    result = []
    for date in top_dates:
        # Determinar el usuario más frecuente para cada fecha
        top_user = max(user_details[date], key=user_details[date].get)
        result.append((str(date), top_user))

    return result


