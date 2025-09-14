from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# @method_decorator(login_required, name='dispatch')
class SobreView(View):
    template_name = 'model/sobre.html'

    def get(self, request, *args, **kwargs):

        context = {}

        return render(request, self.template_name, context)