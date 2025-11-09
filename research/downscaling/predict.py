# predict.py

import sys
import joblib
import pandas as pd

from config import (
    BASE_PATH,
)

def predict_precipitation(ano, mes, lat, lon):
    """
    Faz a predição de precipitação com base em ano, mês, latitude e longitude.
    """

    model_path = BASE_PATH / "models/statistical_downscaling_spatialization.joblib"

    # Carregar modelo
    print("📦 Carregando modelo...")
    model = joblib.load(model_path)

    # Criar DataFrame de entrada
    X_input = pd.DataFrame([{
        'ano': ano,
        'mes': mes,
        'lat': lat,
        'lon': lon
    }])

    # Fazer previsão
    pred = model.predict(X_input)[0]

    print(f"✅ Precipitação prevista de {pred:.2f} milímetros.\n")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("❌ Uso: python3 predict.py <ano> <mes> <latitude> <longitude>\n")
        sys.exit(1)

    try:
        ano = int(sys.argv[1])
        mes = int(sys.argv[2])
        lat = float(sys.argv[3])
        lon = float(sys.argv[4])

        predict_precipitation(ano, mes, lat, lon)

    except ValueError:
        print("❌ Erro: os argumentos devem ser numéricos.\n")
