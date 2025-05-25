# 🌧️ Rainscale

Rainscale é uma aplicação web monolítica desenvolvida em Django para geração de séries temporais de precipitação com base em coordenadas geográficas. A previsão é feita utilizando modelos de aprendizado de máquina treinados previamente. A plataforma oferece uma interface intuitiva com mapa interativo, geração automática de CSVs armazenando a série temporal e páginas auxiliares para guiar o usuário.

Projeto containerizado com Docker + Docker Compose, usando PostgreSQL como banco de dados e tecnologias modernas como JavaScript, Bootstrap e OpenStreetMap.

## 🚀 Como executar localmente

**Pré-requisitos**

- Docker

- Docker Compose

**Passos**

```shell
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ python3 manage.py migrate
$ python3 manage.py makemigrations
$ python3 manage.py collectstatic
$ python3 manage.py runserver
```
