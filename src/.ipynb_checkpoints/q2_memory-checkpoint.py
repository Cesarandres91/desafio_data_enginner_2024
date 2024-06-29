from typing import List, Tuple
from datetime import datetime
import time
import pandas as pd
import json
import os
import re
import memory_profiler

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    # Definir el patrón de búsqueda de emojis utilizando una expresión regular
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F700-\U0001F77F"  # alchemical symbols
        u"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        u"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        u"\U0001FA00-\U0001FA6F"  # Chess Symbols
        u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        "]+", flags=re.UNICODE)

    # Inicializar un diccionario para contar los emojis
    emoji_counts = {}

    # Procesar el DataFrame en chunks para optimizar el uso de memoria
    for chunk in pd.read_json(file_path, lines=True, chunksize=10000):
        # Extraer emojis de la columna 'content'
        for text in chunk['content']:
            emojis = emoji_pattern.findall(text)
            for emoji in emojis:
                emoji_counts[emoji] = emoji_counts.get(emoji, 0) + 1

    # Ordenar los emojis por frecuencia y seleccionar los top 10
    top_emojis = sorted(emoji_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    return top_emojis

