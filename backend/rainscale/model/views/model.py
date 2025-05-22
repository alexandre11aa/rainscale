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

        models = Model.all_objects.filter(is_active=True)

        paises, regioes, modelos = [], [], []
        
        for model in models:

            paises.append({
                'id': model.regiao.nacao.id, 
                'nome': model.regiao.nacao.nome
            })

            regioes.append({
                'id': model.regiao.id, 
                'nome': model.regiao.nome, 
                'pais_id': model.regiao.nacao.id
            })

            modelos.append({
                'id': model.id,
                'nome': model.nome,
                'regiao_id': model.regiao.id
            })

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

        model = get_object_or_404(Model, id=model_id)

        context = {
            'map': True,
            'pais': model.regiao.nacao.nome,
            'regiao': model.regiao.nome,
            'modelo': model.nome
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
