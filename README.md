# 🌧️ Rainscale

Rainscale é uma aplicação web monolítica desenvolvida em Django para geração de séries temporais de precipitação influenciadas por mudanças climáticas com base em coordenadas geográficas. A previsão é feita utilizando modelos de aprendizado de máquina treinados previamente. A plataforma oferece uma interface intuitiva com mapa interativo, geração automática de CSVs armazenando a série temporal e páginas auxiliares para guiar o usuário.

Projeto containerizado com Docker + Docker Compose, usando SQLite como banco de dados e tecnologias modernas como JavaScript, Bootstrap e OpenStreetMap. Acesse o sistema online [**clicando aqui**](https://rainscale.pythonanywhere.com/)! (Caso o site não esteja no ar, entre em contato para que eu o reative.)

## 📁 Estrutura do Projeto

```shell
rainscale/
├── research/              # Estudo de caso de geração de modelos
├── web/                   # Código-fonte do site Django
├── docker-compose.yml     # Orquestração dos containers
├── Dockerfile.backend     # Dockerfile do projeto
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

## 🗺️ Funcionalidades

**Páginas da ferramenta**

- 🔍 *Busca por modelo: selecione o país*, a região e o modelo desejado;

- 🗺️ *Mapa interativo (OpenStreetMap)*: fornece com um clique os pontos de latitude e longitude;

- 📥 *Download em CSV*: gere a previsão e obtenha o arquivo desta o baixando;

- 📚 *Página de tutorial*: guia passo a passo de como utilizar a plataforma;

- 👤 *Página sobre o autor*: provém informações sobre o desenvolvedor do projeto;

- 🔐 *Área administrativa*: painel admin do Django para gerenciamento dos dados (restrito a administradores).

**Como usar**

1. Na página inicial, selecione e busque um modelo a partir de seu país e região;  

2. Na página do modelo, digite uma latitude e longitude ou às obtenha pelo mapa interativo;  

3. Por fim, obtenha o CSV da série temporal de precipitação para a localidade escolhida.

## 🚀 Como executar localmente

**Pré-requisitos**

- Docker

- Docker Compose

**Passos**

1. Clone o repositório:

```shell
$ git clone https://github.com/alexandre11aa/rainscale.git
```

2. Siga para a branch `main`:

```shell
$ git checkout main
```

3. Suba os containers:

```shell
$ docker-compose up --build
```

4. Acesse a aplicação no navegador:

```shell
http://localhost:8000
```

## 📚 Estudo de Caso

A pasta `research/` contém a documentação técnica e os notebooks utilizados na criação do modelo de aprendizado de máquina, incluindo:

1. Coleta dos dados;
2. Pré-processamento de dados;
3. Seleção de atributos;
4. Treinamento e validação do modelo;
5. Métricas de desempenho;
6. Justificativas do modelo final utilizado.

## 🌐 Acesso Online

A aplicação está hospedada no PythonAnywhere, podendo ser acessada através de:

🔗 https://rainscale.pythonanywhere.com/
