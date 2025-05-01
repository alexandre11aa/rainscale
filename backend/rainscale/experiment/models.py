from django.db import models

from core.common.models import BaseModel

from experiment.choices import (
    ACTIVITY_CHOICES,
    DATA_NODE_CHOICES,
    SOURCE_CHOICES,
    INSTITUTION_CHOICES,
    SOURCE_TYPE_CHOICES,
    EXPERIMENT_CHOICES,
    SUB_EXPERIMENT_CHOICES,
    NOMINAL_RESOLUTION_CHOICES,
    VARIANT_LABEL_CHOICES,
    GRID_LABEL_CHOICES,
    TABLE_CHOICES,
    FREQUENCY_CHOICES,
    REALM_CHOICES,
    VARIABLE_CHOICES,
    VARIABLE_UNIT_CHOICES,
    CF_STANDARD_CHOICES
)


class Simulation(BaseModel):
    '''
    Modelo Representativo de Simulação Climática

    Atributos:
        id (int): Chave primária (automático);
        nome (str): Nome da simulação;
        activity (str): Projeto/atividade do CMIP6;
        data_node (str): Servidor de origem dos dados;
        source (str): Nome do modelo climático;
        institution (str): Instituição responsável;
        source_type (str): Tipo de modelo;
        experiment (str): Experimento simulado;
        sub_experiment (str): Sub-experimento;
        nominal_resolution (str): Resolução espacial;
        variant_label (str): Identificador de variante do modelo;
        grid_label (str): Tipo de grade espacial;
        table (str): Tabela de frequência/variável;
        frequency (str): Frequência temporal dos dados;
        realm (str): Domínio do modelo (atmos, ocean...);
        variable (str): Nome da variável modelada;
        variable_unit (str): Unidade da variável modelada;
        cf_standard_name (str): Nome padrão CF da variável;
        version (str): Versão dos dados;
        date_init (date): Data inicial da simulação;
        date_end (date): Data final da simulação;
        
        link (str): Caminho de referência da simulação;
        ref (str): Referência da simulação;
    '''

    nome = models.CharField('Nome da Simulação', max_length=255)
    activity = models.CharField('Atividade', max_length=50, choices=ACTIVITY_CHOICES)
    data_node = models.CharField('Data Node', max_length=50, choices=DATA_NODE_CHOICES)
    source = models.CharField('Modelo (Source)', max_length=50, choices=SOURCE_CHOICES)
    institution = models.CharField('Instituição', max_length=50, choices=INSTITUTION_CHOICES)
    source_type = models.CharField('Tipo de Modelo (Source Type)', max_length=50, choices=SOURCE_TYPE_CHOICES)
    experiment = models.CharField('Experimento', max_length=50, choices=EXPERIMENT_CHOICES)
    sub_experiment = models.CharField('Sub-experimento', max_length=50, default='none', choices=SUB_EXPERIMENT_CHOICES)
    nominal_resolution = models.CharField('Resolução Nominal', max_length=50, choices=NOMINAL_RESOLUTION_CHOICES)
    variant_label = models.CharField('Variant Label', max_length=50, choices=VARIANT_LABEL_CHOICES)
    grid_label = models.CharField('Grid Label', max_length=50, choices=GRID_LABEL_CHOICES)
    table = models.CharField('Tabela (Table)', max_length=50, choices=TABLE_CHOICES)
    frequency = models.CharField('Frequência', max_length=50, choices=FREQUENCY_CHOICES)
    realm = models.CharField('Domínio (Realm)', max_length=50, choices=REALM_CHOICES)
    variable = models.CharField('Variável', max_length=50, choices=VARIABLE_CHOICES)
    variable_unit = models.CharField('Unidade da Variável', max_length=50, choices=VARIABLE_UNIT_CHOICES)
    cf_standard = models.CharField('Padrão CF', max_length=50, choices=CF_STANDARD_CHOICES)
    version = models.CharField('Versão', max_length=50, default='latest')
    date_init = models.DateField('Data Inicial')
    date_end = models.DateField('Data Final')

    link = models.CharField('Caminho para Dados Locais', max_length=255)
    ref = models.CharField('Referência dos Dados Locais', max_length=255)

    def __str__(self):
        return f"{self.nome}"


class LocalData(BaseModel):
    '''
    Modelo Representativo de Dados Locais

    Atributos:
        id (int)*: Chave primária;
        nome (str)*: Nome dos dados locais;

        temporalidade (str): Frequência temporal dos dados;
        variavel (str): Identificador da variável;
        variavel_unidade (str): Unidade da variável;
        data_inicio (DateTimeField): Data de início dos dados locais;
        data_fim (DateTimeField): Data de término dos dados locais;
        
        lat_maxima (float): Latitude Máxima dos dados locais;
        lat_minima (float): Latitude Mínima dos dados locais;
        lon_maxima (float): Longitude Máxima dos dados locais;
        lon_minima (float): Longitude Mínima dos dados locais.
        
        link (str): Caminho de referência dos dados locais;
        ref (str): Referência dos dados locais;
    '''

    nome = models.CharField('Nome dos dados locais', max_length=255)

    temporalidade = models.CharField('Temporalidade da Variavel', max_length=50, choices=FREQUENCY_CHOICES)
    variavel = models.CharField('Variável', max_length=50, choices=VARIABLE_CHOICES)  
    variavel_unidade = models.CharField('Unidade da Variável', max_length=50, choices=VARIABLE_UNIT_CHOICES)
    data_inicio = models.DateTimeField('Data de Início')
    data_fim = models.DateTimeField('Data de Término')

    lat_maxima = models.DecimalField('Latitude Máxima do Modelo', max_digits=10, decimal_places=2)
    lat_minima = models.DecimalField('Latitude Mínima do Modelo', max_digits=10, decimal_places=2)
    lon_maxima = models.DecimalField('Longitude Máxima do Modelo', max_digits=10, decimal_places=2)
    lon_minima = models.DecimalField('Longitude Mínima do Modelo', max_digits=10, decimal_places=2)

    link = models.CharField('Caminho para Dados Locais', max_length=255)
    ref = models.CharField('Referência dos Dados Locais', max_length=255)

    def __str__(self):
        return f"{self.nome}"