from typing import List, Tuple
from datetime import datetime
import time
import pandas as pd
import json
import os
import re
import memory_profiler

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    
    df = pd.read_json(file_path, lines=True)
    mentions_pattern = re.compile(r"@\w+")
    mention_counts = {}
    
    # Recorrer todos los textos de los tweets y contar menciones
    for text in df['content']:
        mentions = mentions_pattern.findall(text)
        for mention in mentions:
            if mention in mention_counts:
                mention_counts[mention] += 1
            else:
                mention_counts[mention] = 1
    # Ordenar las menciones por frecuencia y extraer las top 10
    top_mentions = sorted(mention_counts.items(), key=lambda item: item[1], reverse=True)[:10]
  
    return top_mentions

