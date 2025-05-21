from django.db import models

from core.common.models import BaseModel

from experiment.choices import (
    FREQUENCY_CHOICES, 
    VARIABLE_CHOICES, 
    VARIABLE_UNIT_CHOICES
)

from user.models import CustomUser
from location.models import Region
from experiment.models import (
    Simulation, 
    LocalData
)


class Model(BaseModel):
    '''
    Modelo Representativo de Modelos de Aprendizado de Máquinas

    Atributos:
        id (int)*: Chave primária;

        regiao (int)*: Chave que associa Modelo à Região;
        autor (int)*: Chave que associa Modelo à Autor;

        simulacoes (list[Simulation]): Lista de simulações climáticas associadas;
        dados_locais (list[LocalData]): Lista de conjuntos de dados locais associados;

        nome (str)*: Nome do Modelo;
        temporalidade (str): Frequência temporal dos dados;
        variavel (str): Identificador da variável;
        variavel_unidade (str): Unidade da variável;
        pontos [.csv] (file): Pontos Usados na Espacialização do Modelo (lat, lon, fonte);
        modelo [.pkl ou .h5] (file): Modelo de Aprendizado de Máquina;
        caderno [.ipynb] (file): Caderno de Desenvolvimento do Modelo;
        repositorio (str): Repositório do Modelo;

        lat_maxima (float): Latitude Máxima do Modelo;
        lat_minima (float): Latitude Mínima do Modelo;
        lon_maxima (float): Longitude Máxima do Modelo;
        lon_minima (float): Longitude Mínima do Modelo.
    '''

    regiao = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='modelo')
    autor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='modelo')

    simulacoes = models.ManyToManyField(Simulation, blank=True, related_name='modelo')
    dados_locais = models.ManyToManyField(LocalData, blank=True, related_name='modelo')

    nome = models.CharField('Nome do Modelo', max_length=255)
    temporalidade = models.CharField('Temporalidade da Variavel', max_length=50, choices=FREQUENCY_CHOICES)
    variavel = models.CharField('Variável', max_length=50, choices=VARIABLE_CHOICES)  
    variavel_unidade = models.CharField('Unidade da Variável', max_length=50, choices=VARIABLE_UNIT_CHOICES)
    pontos = models.FileField('Pontos do Modelo', upload_to='points/')
    modelo = models.FileField('Modelo de Aprendizado de Máquina', upload_to='models/')
    caderno = models.FileField('Caderno de Modelo', upload_to='notebooks/', blank=True, null=True)
    repositorio = models.CharField('Repositório do Modelo', max_length=255, blank=True, null=True)
    
    lat_maxima = models.DecimalField('Latitude Máxima do Modelo', max_digits=10, decimal_places=2)
    lat_minima = models.DecimalField('Latitude Mínima do Modelo', max_digits=10, decimal_places=2)
    lon_maxima = models.DecimalField('Longitude Máxima do Modelo', max_digits=10, decimal_places=2)
    lon_minima = models.DecimalField('Longitude Mínima do Modelo', max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nome}"