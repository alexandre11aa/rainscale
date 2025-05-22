from django.contrib import messages


def feedback_message(request, dados):

    if messages.get_messages(request):

        title, text = str(list(messages.get_messages(request))[0]).split('|')

        if list(messages.get_messages(request))[0].tags == 'success':
            dados['title_sucess'] = title
            dados['text_sucess']= text

        else:
            dados['title_error'] = title
            dados['text_error'] = text

    return dados
