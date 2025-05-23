from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from model.models import Model

from model.forms.mapa import MapaForm


# @method_decorator(login_required, name='dispatch')
class MapaView(View):
    template_name = 'model/mapa.html'
    success_url = reverse_lazy('mapa')
    get_url = reverse_lazy('mapa')

    def get_datas(self, model):

        dados_modelo = (
            model.regiao.nacao.nome,
            model.regiao.nome,
            model.autor.nome,
            model.nome,
            model.temporalidade,
            model.variavel,
            model.variavel_unidade,
            model.pontos,
            model.modelo,
            model.caderno,
            model.repositorio,
            model.lat_maxima,
            model.lat_minima,
            model.lon_maxima,
            model.lon_minima
        )

        dados_experimentos = []

        for experimento in model.simulacoes.all():
        
            dados_experimentos.append((
                experimento.nome,
                experimento.activity,
                experimento.data_node,
                experimento.source,
                experimento.institution,
                experimento.source_type,
                experimento.experiment,
                experimento.sub_experiment,
                experimento.nominal_resolution,
                experimento.variant_label,
                experimento.grid_label,
                experimento.table,
                experimento.frequency,
                experimento.realm,
                experimento.variable,
                experimento.variable_unit,
                experimento.cf_standard,
                experimento.version,
                experimento.date_init,
                experimento.date_end,
                experimento.link,
                experimento.ref
            ))

        dados_locais = []

        for dado_local in model.dados_locais.all():

            dados_locais.append((
                dado_local.nome,
                dado_local.temporalidade,
                dado_local.variavel,
                dado_local.variavel_unidade,
                dado_local.data_inicio,
                dado_local.data_fim,
                dado_local.lat_maxima,
                dado_local.lat_minima,
                dado_local.lon_maxima,
                dado_local.lon_minima,
                dado_local.link,
                dado_local.ref
            ))
        
        context = {
            'map': True,
            'model_id': model.id,
            'pais': model.regiao.nacao.nome,
            'regiao': model.regiao.nome,
            'modelo': model.nome,
            'dados_modelo': dados_modelo,
            'dados_experimentos': dados_experimentos,
            'dados_locais': dados_locais
        }

        return context

    def get(self, request, *args, **kwargs):

        model_id = kwargs.get('model_id')

        context = self.get_datas(
            get_object_or_404(Model, id=model_id)
        )

        context['form'] = MapaForm()

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        
        print(request)

        return redirect('index')