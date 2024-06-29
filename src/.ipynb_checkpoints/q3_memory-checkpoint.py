from typing import List, Tuple
from datetime import datetime
import time
import pandas as pd
import json
import os
import re
import memory_profiler

def q3_memory(file_path: str) -> List[Tuple[str, int]]:

    # Compilar la expresión regular para las menciones de usuarios
    mentions_pattern = re.compile(r'@\w+')

    # Diccionarios para mantener conteos de menciones
    mention_counts = {}

    # Procesar el archivo en chunks para reducir el uso de memoria
    for chunk in pd.read_json(file_path, lines=True, chunksize=10000):
        # Extraer y contar menciones en cada chunk
        for text in chunk['content']:
            mentions = mentions_pattern.findall(text)
            for mention in mentions:
                mention_counts[mention] = mention_counts.get(mention, 0) + 1

    # Ordenar las menciones por su frecuencia y obtener las top 10
    top_mentions = sorted(mention_counts.items(), key=lambda item: item[1], reverse=True)[:10]

    return top_mentions