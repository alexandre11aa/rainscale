# 🌧️ Rainscale

Este projeto implementa um modelo de aprendizado de máquina (AM) para realizar **downscaling estatístico** de dados de precipitação na Paraíba, utilizando dados observados (AESA) e simulados (CMIP6). O objetivo é prever chuvas futuras até o ano de 2100 com base em modelos climáticos globais ajustados para escala local.

## 📁 Estrutura de Pastas

A estrutura geral do projeto é apresentada abaixo:

```bash
rainscale/            # Diretório raiz;
|-- datas/            # Dados do projeto (.csv .geojson .nc);
|   |-- external/     # Dados de fontes externas;
|   |-- interim/      # Dados intermediários;
|   |-- processed/    # Dados finais;
|   `-- raw/          # Dados originais;
|-- downscaling/      # Código-fonte do projeto;
|   |-- __init__.py   # Torna o diretório um pacote Python;
|   |-- config.py     # Arquivo de configuração geral;
|   |-- predict.py    # Previsões com modelo treinado;
|   `-- train.py      # Treinamento dos modelos;
|-- models/           # Modelos treinados (.joblib .h5);
|-- notebooks/        # Jupyter Notebooks (.ipynb);
|-- manage.py         # Script para automatizar tarefas;
|-- README.md         # Documento explicativo do projeto;
`-- requirements.txt  # Lista de dependências.
```

## ⚙️ Gerenciamento com manage.py

O arquivo `manage.py` automatiza tarefas comuns como criação de ambiente virtual, instalação de dependências, treinamento e predição. Para mais informações sobre os comandos, digite no console:

```bash
$ python manage.py
```

## 🧰 Dependências

As bibliotecas necessárias estão listadas em `requirements.txt`. Para instalá-las manualmente:  

```bash
$ pip install -r requirements.txt
```
