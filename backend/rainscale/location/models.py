from django.db import models

from core.common.models import BaseModel


class Nation(BaseModel):
    '''
    Modelo Representativo de País

    Atributos:
        id (int)*: Chave primária;
        nome (str)*: Nome do País;
        contorno (json): Contorno do País;
        lat_maxima (float): Latitude Máxima do País;
        lat_minima (float): Latitude Mínima do País;
        lon_maxima (float): Longitude Máxima do País;
        lon_minima (float): Longitude Mínima do País;
    '''
   
    nome = models.CharField('Nome do País', max_length=255)
    
    contorno = models.JSONField('Contorno do País (.json)', blank=True, null=True)
    
    lat_maxima = models.DecimalField('Latitude Máxima do País', max_digits=10, decimal_places=2, blank=True, null=True)
    lat_minima = models.DecimalField('Latitude Mínima do País', max_digits=10, decimal_places=2, blank=True, null=True)
    lon_maxima = models.DecimalField('Longitude Máxima do País', max_digits=10, decimal_places=2, blank=True, null=True)
    lon_minima = models.DecimalField('Longitude Mínima do País', max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.nome
    

class Region(BaseModel):
    '''
    Modelo Representativo de Região

    Atributos:
        id (int)*: Chave primária;
        nacao (int)*: Chave que associa Região à País;
        nome (str)*: Nome da Região;
        contorno (json): Contorno da Região;
        lat_maxima (float): Latitude Máxima da Região;
        lat_minima (float): Latitude Mínima da Região;
        lon_maxima (float): Longitude Máxima da Região;
        lon_minima (float): Longitude Mínima da Região;
    '''
   
    nacao = models.ForeignKey(Nation, on_delete=models.CASCADE, related_name='regiao')

    nome = models.CharField('Nome da Região', max_length=255)
    
    contorno = models.JSONField('Contorno da Região', blank=True, null=True)
    
    lat_maxima = models.DecimalField('Latitude Máxima da Região', max_digits=10, decimal_places=2, blank=True, null=True)
    lat_minima = models.DecimalField('Latitude Mínima da Região', max_digits=10, decimal_places=2, blank=True, null=True)
    lon_maxima = models.DecimalField('Longitude Máxima da Região', max_digits=10, decimal_places=2, blank=True, null=True)
    lon_minima = models.DecimalField('Longitude Mínima da Região', max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.nome