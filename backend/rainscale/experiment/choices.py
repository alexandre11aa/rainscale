ACTIVITY_CHOICES = [
    ('UNK', 'Desconhecido'),
    ('ScenarioMIP', 'CMIP')
]

DATA_NODE_CHOICES = [
    ('UNK', 'Desconhecido'),
    ('esgf-data1.llnl.gov', 'esgf-data1.llnl.gov')    # Data node do Earth System Grid Federation, mantido pelo Lawrence Livermore National Laboratory (LLNL)
]

SOURCE_CHOICES = [
    ('UNK', 'Desconhecido'),
    ('CNRM-CM6-1-HR', 'CNRM-CM6-1-HR')                # Modelo climático: Centre National de Recherches Météorologiques - CMIP6 - Version 1 - High Resolution
]

INSTITUTION_CHOICES = [
    ('UNK', 'Desconhecido'),
    ('CNRM-CERFACS', 'CNRM-CERFACS')                  # Centre National de Recherches Météorologiques - Centre Européen de Recherche et de Formation Avancée en Calcul Scientifique
]

SOURCE_TYPE_CHOICES = [
    ('UNK', 'Desconhecido'),
    ('AOGCM', 'Atmosphere-Ocean General Circulation Model')
]

EXPERIMENT_CHOICES = [
    ('UNK', 'Desconhecido'),
    ('ssp585', 'SSP5-85')
]

SUB_EXPERIMENT_CHOICES = [
    ('UNK', 'Desconhecido')
]

NOMINAL_RESOLUTION_CHOICES = [
    ('UNK', 'Desconhecido'),
    ('10 km', '10 km'),
    ('25 km', '25 km'),
    ('50 km', '50 km'),
    ('100 km', '100 km'),
    ('200 km', '200 km'),
    ('250 km', '250 km'),
    ('500 km', '500 km'),
    ('10000 km', '10000 km'),
    ('1x1 degree', '1x1 grau'),
    ('2x2 degree', '2x2 graus'),
]

VARIANT_LABEL_CHOICES = [
    ('UNK', 'Desconhecido'),
    ('r1i1p1f2', 'r1i1p1f2')                          # r1i1p1f2 - 1ª realização, 1ª inicialização, 1ª forçante, 2ª configuração de modelo
]

GRID_LABEL_CHOICES = [
    ('UNK', 'Desconhecido'),
    ('gm', 'Grade global (Global grid)'),             # Grade global, geralmente usada em modelos climáticos globais
    ('gn', 'Grade do modelo (Grid native)'),          # Grade nativa do modelo (usada diretamente no modelo climático)
    ('gr', 'Grade regular (Regular grid)'),           # Grade regular, com uma interpolação bilinear dos dados
    ('gr1', 'Grade 1 (Resolution 1)'),                # Primeira resolução de grade, pode variar dependendo do modelo
    ('gr2', 'Grade 2 (Resolution 2)'),                # Segunda resolução de grade
    ('gr3', 'Grade 3 (Resolution 3)'),                # Terceira resolução de grade
    ('gra', 'Grade ajustada (Adjusted grid)'),        # Grade ajustada em relação a um modelo ou área específica
    ('grg', 'Grade geofísica (Geophysical grid)'),    # Grade geofísica usada para representar dados relacionados a variáveis geofísicas
    ('grz', 'Grade zonal (Zonal grid)'),              # Grade zonal, pode se referir a uma grade que foca em uma faixa específica de latitude
    ('gr1z', 'Grade 1 zonal (Resolution 1 zonal)'),   # Grade de resolução 1 em uma configuração zonal
    ('gr2z', 'Grade 2 zonal (Resolution 2 zonal)')    # Grade de resolução 2 em uma configuração zonal
]

TABLE_CHOICES = [
    ('UNK', 'Desconhecido'),
    ('day', 'Diário')
]

FREQUENCY_CHOICES = [
    ('UNK', 'Desconhecido'),
    ('1hr', '1 hora'),                                # Dados disponíveis a cada 1 hora
    ('1hrCM', '1 hora (climate model)'),              # Saída horária centrada em variáveis do modelo climático
    ('1hrPt', '1 hora (ponto)'),                      # Dados horários em um ponto específico (station-like)
    ('3hr', '3 horas'),                               # Dados disponíveis a cada 3 horas
    ('3hrPt', '3 horas (ponto)'),                     # Dados a cada 3 horas em um ponto específico
    ('6hr', '6 horas'),                               # Dados disponíveis a cada 6 horas
    ('6hrPt', '6 horas (ponto)'),                     # Dados a cada 6 horas em um ponto específico
    ('day', 'Diário'),                                # Dados diários
    ('dec', 'Década'),                                # Médias ou totais por década (10 anos)
    ('fx', 'Fixo'),                                   # Variáveis fixas no tempo (ex: topografia, uso do solo)
    ('mon', 'Mensal'),                                # Dados mensais
    ('monC', 'Mensal (climatologia)'),                # Climatologia mensal (média de meses ao longo de vários anos)
    ('monPt', 'Mensal (ponto)'),                      # Dados mensais em um ponto específico
    ('month', 'Mensal (alternativo)'),                # Variante não padronizada de "mon" (rara)
    ('subhrPt', 'Sub-horário (ponto)'),               # Dados com resolução inferior a 1 hora em ponto específico
    ('yr', 'Anual'),                                  # Dados anuais
    ('yrPt', 'Anual (ponto)')                         # Dados anuais em um ponto específico
]

REALM_CHOICES = [
    ('UNK', 'Desconhecido'),
    ('aerosol', 'Aerosol'),                           # Dados relacionados a aerossóis atmosféricos
    ('atmos', 'Atmosfera'),                           # Dados da atmosfera (pressão, temperatura, vento, etc.)
    ('atmosChem', 'Química Atmosférica'),             # Dados da composição química da atmosfera (ex: ozônio, NOx, CO2)
    ('land', 'Terra'),                                # Superfície terrestre (solo, vegetação, umidade do solo, etc.)
    ('landIce', 'Geleiras Terrestres'),               # Calotas polares e geleiras em terra firme
    ('ocean', 'Oceano'),                              # Dados do oceano (correntes, temperatura, salinidade, etc.)
    ('ocnBgChem', 'Química Biogeoquímica Oceânica'),  # Ciclos de carbono, oxigênio e nutrientes no oceano
    ('sea', 'Mar'),                                   # Dados do mar (geralmente pouco usado ou redundante com ocean)
    ('seaIce', 'Gelo Marinho')                        # Gelo flutuante sobre o oceano (concentração, espessura, extensão)
]

VARIABLE_CHOICES = [
    ('UNK', 'Desconhecido'),
    ('pr', 'Precipitação'),
    ('pr_acum', 'Precipitação Acumulada'),
]

VARIABLE_UNIT_CHOICES = [
    ('UNK', 'Desconhecido'),
    ('mm', 'mm'),
    ('kg m-2 s-1', 'kg m-2 s-1'),
]

CF_STANDARD_CHOICES = [
    ('UNK', 'Desconhecido'),
    ('precipitation_flux', 'Fluxo de Precipitação'),
]