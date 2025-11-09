# train.py

import joblib
import pandas as pd

from sklearn.ensemble import ExtraTreesRegressor

from config import (
    BASE_PATH,
    DATABASE_TYPE, 
    DATABASE_GENERATE,
)

def train_model(database_type="sum", database_generate=True):
    """
    Treina e salva o modelo de espacialização do ExtraTreesRegressor para o downscaling estatístico.
    
    Parâmetros:
        database_type (str): tipo de base de dados (ex: 'train', 'test', etc.)
        databases_generate (bool): se True, salva o modelo treinado.
    """

    # Caminho para a base de dados
    csv_path = BASE_PATH / f'datas/processed/4.3.4_downscaling_database/aesa_to_cnrm_cm6_1hr_{database_type}_downscaling_database.csv'
    
    print(f"📂 Carregando base de dados: {csv_path}")

    # Carregando base de dados
    df_aesa_best_model = pd.read_csv(csv_path)

    # Definindo features (X) e variável alvo (y)
    X_col = [col for col in df_aesa_best_model.columns if col not in ['pr_local']]
    y_col = 'pr_local'

    X = df_aesa_best_model[X_col].copy()
    y = df_aesa_best_model[y_col].copy()

    # Melhores hiperparâmetros
    best_params = {
        'max_depth': 20,  # reduzido para compactação do modelo
        'max_features': 2,
        'min_samples_leaf': 1,
        'min_samples_split': 2,
        'n_estimators': 20  # reduzido para armazenamento
    }

    print("🚀 Treinando modelo...")

    model = ExtraTreesRegressor(**best_params, random_state=7)
    model.fit(X, y)

    if database_generate:
        model_path = BASE_PATH / f'models/statistical_downscaling_spatialization.joblib'
        joblib.dump(model, model_path, compress=3)
        print(f"✅ Modelo salvo em: {model_path}\n")
    else:
        print("✅ Treinamento concluído, mas o modelo não foi salvo (databases_generate=False).\n")

if __name__ == "__main__":
    train_model(DATABASE_TYPE, DATABASE_GENERATE)
