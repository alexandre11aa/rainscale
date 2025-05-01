import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from core.common.models import BaseModel, UserManager


class CustomUser(AbstractBaseUser, PermissionsMixin, BaseModel):
    '''
    Modelo Representativo de Usuário

    Atributos:
        id (int)*: Chave primária;
        uuid (str)*: Chave única no formato UUID;
        nome (str)*: Nome do usuário;
        email (str)*: Email do usuário;
        github (str): Github do usuário;
        portfolio (str)*: Portfólio do usuário;
    '''
        
    uuid = models.UUIDField("Código UUID", default=uuid.uuid4, editable=False)
    
    nome = models.CharField('Nome do Usuário', max_length=255)
    email = models.EmailField('Email do Usuário', unique=True)
    github = models.CharField('Github do Usuário', max_length=255)
    portfolio = models.EmailField('Portfólio do Usuário', unique=True)
    
    is_staff = models.BooleanField('Is Staff', default=False)
    is_superuser = models.BooleanField('Is Superuser', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    objects = UserManager()

    def __str__(self):
        return self.nome