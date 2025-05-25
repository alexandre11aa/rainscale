from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import render
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