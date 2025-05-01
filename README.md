# Rainscale

Monolito Django.

O Downscaling Estatístico funciona da seguinte forma:

Pega-se os preditandos, que são os GCMs com cenários climáticos SSPs definidos do CMIP6. Esses dados vão dos anos 2000 à 2100 e possuem precipitação, data e localização.

A partir deles pega-se os preditores, que são as precipitações dos postos locais que vão de 2000 à 2025 com dados de precipitação, data e localização.

Cria-se então uma nova coluna de forma a associar os dados dos GCM's com os dos postos locais, que é a distância entre o posto pluviométrico ao ponto do GCM. Os postos pluviométricos se associarão ao GCM mais próximo que estejam na mesma data, ou seja, será criado na tabela dos postos pluviométricos novas colunas, com as antigas linhas adquirindo os dados do ponto do GCM mais próximo que possuam a mesma data.

Com isso, os dados unidos irão de 2000 à 2025, onde dados que vão de 2000 à 2019 (aproximadamente 70%) serão usados para treino, e de 2000 à 2025 (aproximadamente 30%) serão usados para teste.

Com o modelo de downscaling treinado, será feito a predição do restante dos dados dos postos pluviométricos locais para até o ano de 2100.

Após toda a predição realizada, será feita a espacialização dos dados locais gerados até o ano de 2100, de forma a ser possível a partir da latitude e longitude de um local dentro do espaço espacializado, gerar uma série temporal que vai de 2000 à 2100.