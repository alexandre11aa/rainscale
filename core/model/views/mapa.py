import json
import joblib
import pandas as pd

from io import StringIO

from django.http import HttpResponse
from django.views import View
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from core.common.utils import (
    feedback_message,
    gerador_de_df
)

from model.models import Model
from model.forms.mapa import MapaForm


# @method_decorator(login_required, name='dispatch')
class MapaView(View):
    template_name = 'model/mapa.html'

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

        lista_de_pontos, fontes_unicas = [], []
        
        if model.pontos:

            df = pd.read_csv(model.pontos)

            fontes_unicas = df['fonte'].unique().tolist()

            cores = [
                "#1f77b4",  # azul
                "#ff7f0e",  # laranja
                "#2ca02c",  # verde
                "#d62728",  # vermelho
                "#9467bd",  # roxo
                "#8c564b",  # marrom
                "#e377c2",  # rosa
                "#7f7f7f",  # cinza
                "#bcbd22",  # amarelo esverdeado
                "#17becf"   # ciano
            ]

            fontes_unicas = [
                (fonte, cores[i % len(cores)]) 
                for i, fonte in enumerate(fontes_unicas)
            ]

            lista_de_pontos = list(
                df.itertuples(index=False, name=None)
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
            'latitude_central': (model.lat_maxima + model.lat_minima) / 2,
            'longitude_central': (model.lon_maxima + model.lon_minima) / 2,
            'lista_de_pontos': json.dumps(lista_de_pontos),
            'fontes_unicas': json.dumps(fontes_unicas),
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

        context = feedback_message(request, context)

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        model_id = kwargs.get('model_id')

        try:

            form = MapaForm(request.POST, model_id=model_id)

            if form.is_valid():
                latitude, longitude = form.get()

            else:
                messages.error(
                    request, f'ERRO|{form.errors.as_text().split("* ")[-1]}'
                )

                return redirect('mapa', model_id)

            model = get_object_or_404(Model, id=model_id)

            if not model.modelo:
                messages.error(
                    request, f'ERRO|O modelo de aprendizado de máquinas ainda não está registrado no sistema. Entre em contato com a administração!'
                )

                return redirect('mapa', model_id)
            
            ml_model = joblib.load(model.modelo)

            df = gerador_de_df(latitude, longitude, 1994, 2100)
            df = df[ml_model.feature_names_in_]

            df['pr_acum'] = ml_model.predict(df)

            csv_buffer = StringIO()

            df.to_csv(csv_buffer, index=False)
            
            csv_buffer.seek(0)

            response = HttpResponse(csv_buffer, content_type='text/csv')

            response['Content-Disposition'] = f'attachment; filename="{model.nome}_{latitude}_{longitude}.csv"'

            return response
    
        except Exception as e:

            messages.error(
                request, f'ERRO|Algum erro inesperado aconteceu, entre em contato com a administração: {e}'
            )

            return redirect('mapa', model_id)