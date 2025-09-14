import pandas as pd

from django.contrib import messages


def feedback_message(request, dados):

    if messages.get_messages(request):

        title, text = str(list(messages.get_messages(request))[0]).split('|')

        if list(messages.get_messages(request))[0].tags == 'success':
            dados['title_success'] = title
            dados['text_success']= text

        else:
            dados['title_error'] = title
            dados['text_error'] = text

    return dados


def gerador_de_df(latitude: float, longitude: float, ano_inicial: float, ano_final: float) -> pd.DataFrame:
    '''
    Gera um DataFrame com colunas: 'latitude', 'longitude', 'ano' e 'mes'.
    Para cada combinação de ano (ano_inicial a ano_final) e mês (1 a 12).
    '''

    dados = []

    for ano in range(int(ano_inicial), int(ano_final) + 1):
        for mes in range(1, 13):
            dados.append({
                'lat': latitude,
                'lon': longitude,
                'ano': ano,
                'mes': mes
            })

    df = pd.DataFrame(dados)

    return df