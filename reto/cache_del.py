import os
import shutil
from pathlib import Path

def limpiar_cache():
    try:
        carpeta_cache = Path(__file__).parent / "__pycache__"
        if carpeta_cache.exists():
            shutil.rmtree(carpeta_cache)
    except:
        pass