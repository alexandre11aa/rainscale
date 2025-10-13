# 🌧️ Rainscale

Rainscale é uma aplicação web monolítica desenvolvida em Django para geração de séries temporais de precipitação com base em coordenadas geográficas. A previsão é feita utilizando modelos de aprendizado de máquina treinados previamente. A plataforma oferece uma interface intuitiva com mapa interativo, geração automática de CSVs armazenando a série temporal e páginas auxiliares para guiar o usuário.

Projeto containerizado com Docker + Docker Compose, usando SQLite como banco de dados e tecnologias modernas como JavaScript, Bootstrap e OpenStreetMap.

## 📁 Estrutura do Projeto

```shell
rainscale/                     # Código-fonte do site Django
├── core/                      # Diretório do projeto Django
│   ├── core/                  # Projeto Django
│   ├── experiment/            # App "experiment"
│   ├── location/              # App "location"
│   ├── model/                 # App "model"
│   ├── user/                  # App "user"
│   ├── static/                # Arquivos estáticos customizados
│   ├── staticfiles/           # Arquivos estáticos coletados
│   ├── templates/             # Templates HTML
│   ├── manage.py              # Gerenciador do Django
│   └── requirements.txt       # Dependências Python
├── LICENSE
└── README.md
```

## 🧰 Tecnologias Utilizadas

**Backend**

- Python

- Django

- SQLite

- Pandas

- Scikit-learn

- Pillow

- Joblib

- ASGIRef, SQLParse

**Frontend**

- Django Templates

- HTML5

- CSS3

- Bootstrap

- JavaScript

- Leaflet.js (com OpenStreetMap)

## 🚀 Como executar localmente

**Pré-requisitos**

- Python 3.11.2

**Passos**

1. Clone o repositório:

```shell
$ git clone https://github.com/alexandre11aa/rainscale.git
```

2. Siga para a branch `main`:

```shell
$ git checkout main
```

3. Siga para o diretório principal e suba os containers:

```shel
$ sudo docker-compose up --build
```

10. Acesse a aplicação no navegador:

```shell
http://localhost:8000
```

## 🌐 Acesso Online

A aplicação está hospedada no PythonAnywhere, podendo ser acessada através de:

🔗 rainscale.pythonanywhere.com