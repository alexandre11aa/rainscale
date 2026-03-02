# 🌧️ Rainscale

Rainscale é uma aplicação web monolítica desenvolvida em Django para geração de séries temporais de precipitação com base em coordenadas geográficas. A previsão é feita utilizando modelos de aprendizado de máquina treinados previamente. A plataforma oferece uma interface intuitiva com mapa interativo, geração automática de CSVs armazenando a série temporal e páginas auxiliares para guiar o usuário.

Projeto hospedado no PythonAnywhere usando SQLite como banco de dados e tecnologias modernas como JavaScript, Bootstrap e OpenStreetMap. Acesse o sistema online [**clicando aqui**](https://rainscale.pythonanywhere.com/)! (Caso o site não esteja no ar, entre em contato para que eu o reative.)

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

2. Siga para a branch `prod`:

```shell
$ git checkout prod
```

3. Declare um novo `DEBUG` em *core/core/settings.py*:

```python
...
26 # SECURITY WARNING: don't run with debug turned on in production!
27 DEBUG = True
28
...
```

4. Declare um novo `ALLOWED_HOSTS` em *core/core/settings.py*:

```python
...
28
29 ALLOWED_HOSTS = ['*']
30
...
```

5. Siga para o diretório *core/core/* e crie um ambiente virtual:

```shel
$ cd core
$ python3 -m venv env
```

6. Ative o ambiente virtual e instale as dependências:

```shel
$ source env/bin/activate
$ pip install -r requirements.txt
```

7. Faça as migrações do banco de dados:

```shel
$ python3 manage.py migrate
$ python3 manage.py makemigrations
```

8. Colete os arquivos estáticos:

```shel
$ python3 manage.py collectstatic
```

9. Inicie o servidor local Django:

```shell
$ python3 manage.py runserver
```

10. Acesse a aplicação no navegador:

```shell
http://localhost:8000
```

## 🌐 Acesso Online

A aplicação está hospedada no PythonAnywhere, podendo ser acessada através de:

🔗 https://rainscale.pythonanywhere.com/
