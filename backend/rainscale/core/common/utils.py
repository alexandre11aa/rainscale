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
