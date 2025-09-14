# Configuração do Django

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from datetime import datetime

from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

from location.models import Nation, Region
from experiment.models import Simulation, LocalData
from user.models import CustomUser
from model.models import Model

# Registrando Dados

try:
    existing_model = Model.objects.get(nome="Rainscale")

    print('Modelo de teste Rainscale ativo.')

except ObjectDoesNotExist:

    nation = Nation.objects.create(
        nome="Brasil",
        lat_maxima=5.27,
        lat_minima=-33.75,
        lon_maxima=-34.79,
        lon_minima=-73.99
    )
    nation.save()

    region = Region.objects.create(
        nacao=nation,
        nome="Paraíba",
        contorno=os.path.join('case_study', 'datas', 'external', 'brazil-paraiba.geojson'),
        lat_maxima=-5.25,
        lat_minima=-8.32,
        lon_maxima=-34.79,
        lon_minima=-38.10
    )
    region.save()

    simulation_historical = Simulation.objects.create(
        nome="pr_day_CNRM-CM6-1-HR_historical_r1i1p1f2_gr_19940101-20141231",
        activity='CMIP',
        data_node='esgf-data1.llnl.gov',
        source='CNRM-CM6-1-HR',
        institution='CNRM-CERFACS',
        source_type='AOGCM',
        experiment='historical',
        sub_experiment='UNK',
        nominal_resolution='50 km',
        variant_label='r1i1p1f2',
        grid_label='gr',
        table='day',
        frequency='day',
        realm='atmos',
        variable='pr',
        variable_unit='kg m-2 s-1',
        cf_standard='precipitation_flux',
        version='20191021',
        date_init=timezone.make_aware(datetime(1994, 1, 1, 0, 0, 0)),
        date_end=timezone.make_aware(datetime(2014, 12, 31, 23, 59, 59)),
        link='#',
        ref='#'
    )
    simulation_historical.save()

    simulation_future = Simulation.objects.create(
        nome='pr_day_CNRM-CM6-1-HR_ssp585_r1i1p1f2_gr_20400101-20641231',
        activity='CMIP',
        data_node='esgf-data1.llnl.gov',
        source='CNRM-CM6-1-HR',
        institution='CNRM-CERFACS',
        source_type='AOGCM',
        experiment='ssp585',
        sub_experiment='UNK',
        nominal_resolution='50 km',
        variant_label='r1i1p1f2',
        grid_label='gr',
        table='day',
        frequency='day',
        realm='atmos',
        variable='pr',
        variable_unit='kg m-2 s-1',
        cf_standard='precipitation_flux',
        version='20191021',
        date_init=timezone.make_aware(datetime(2015, 1, 1, 0, 0, 0)),
        date_end=timezone.make_aware(datetime(2100, 12, 31, 23, 59, 59)),
        link='#',
        ref='#'
    )
    simulation_future.save()

    local_data = LocalData.objects.create(
        nome='Agência Executiva de Gestão das Águas do Estado da Paraíba',
        temporalidade='day',
        variavel='pr',
        variavel_unidade='mm',
        data_inicio=timezone.make_aware(datetime(1994, 1, 1, 0, 0, 0)),
        data_fim=timezone.make_aware(datetime(2023, 12, 31, 23, 59, 59)),
        lat_maxima=-5.25,
        lat_minima=-8.32,
        lon_maxima=-34.79,
        lon_minima=-38.10,
        link='#',
        ref='#'
    )
    local_data.save()

    author = CustomUser.objects.create(
        nome='Alexandre Estrela de Lacerda Nobrega',
        email='alexandrestrelaln@gmail.com',
        github='https://github.com/alexandre11aa',
        portfolio='https://alexandre11aa.github.io/'
    )
    author.save()

    # Criando a instância do Modelo
    model = Model.objects.create(
        regiao=region,
        autor=author,
        nome="Rainscale",
        temporalidade='mon',
        variavel='pr_acum',
        variavel_unidade='mm',
        pontos=None,  # 'OBS: INSERIR MANUALMENTE NO DJANGO ADMIN!'
        modelo=None,  # 'OBS: INSERIR MANUALMENTE NO DJANGO ADMIN!'
        caderno='',
        repositorio='https://github.com/alexandre11aa/rainscale/tree/main/case_study',
        lat_maxima=-6.25,
        lat_minima=-8.32,
        lon_maxima=-34.79,
        lon_minima=-38.10,
    )
    model.simulacoes.add(simulation_historical, simulation_future)
    model.dados_locais.add(local_data)
    model.save()

    print('Modelo de teste Rainscale ativado.')

exit()
