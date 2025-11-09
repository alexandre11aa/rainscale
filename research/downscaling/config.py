# config.py

from pathlib import Path

# Tipo de precipitação a se obter
DATABASE_TYPE = 'sum'

# Gerar nova base de dados ao treinar
DATABASE_GENERATE = False

# Caminho base
BASE_PATH = Path(__file__).resolve().parent.parent