from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from model.models import Model


# @method_decorator(login_required, name='dispatch')
class IndexView(View):
    template_name = 'model/index.html'
    success_url = reverse_lazy('index')
    get_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):

        paises = [
            {'id': 1, 'nome': 'Brasil'},
            {'id': 2, 'nome': 'Argentina'}
        ]

        regioes = [
            {'id': 1, 'nome': 'Paraíba', 'pais_id': 1},
            {'id': 2, 'nome': 'São Paulo', 'pais_id': 1},
            {'id': 3, 'nome': 'Buenos Aires', 'pais_id': 2},
            {'id': 4, 'nome': 'Córdoba', 'pais_id': 2}
        ]

        modelos = [
            {'id': 1, 'nome': 'Modelo A', 'regiao_id': 1},
            {'id': 2, 'nome': 'Modelo B', 'regiao_id': 2},
            {'id': 3, 'nome': 'Modelo C', 'regiao_id': 3},
            {'id': 4, 'nome': 'Modelo D', 'regiao_id': 4}
        ]

        context = {
            'map': False,
            'paises': paises,
            'regioes': regioes,
            'modelos': modelos
        }

        return render(request, self.template_name, context)


# @method_decorator(login_required, name='dispatch')
class MapaView(View):
    template_name = 'model/mapa.html'
    success_url = reverse_lazy('mapa')
    get_url = reverse_lazy('mapa')

    def get(self, request, *args, **kwargs):

        model_id = kwargs.get('model_id')

        #model = get_object_or_404(Model, id=model_id)

        context = {
            'map': True,
            'pais': 'Brasil',
            'regiao': 'Paraíba',
            'modelo': 'Modelo A'
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pass


# @method_decorator(login_required, name='dispatch')
class TutorialView(View):
    template_name = 'model/tutorial.html'

    def get(self, request, *args, **kwargs):

        context = {}

        return render(request, self.template_name, context)


# @method_decorator(login_required, name='dispatch')
class SobreView(View):
    template_name = 'model/sobre.html'

    def get(self, request, *args, **kwargs):

        context = {}

        return render(request, self.template_name, context)
