from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.db.models import Q


@method_decorator(login_required, name='dispatch')
class IndexView(View):
    #form_class = EnderecoForm
    template_name = 'model/index.html'
    success_url = reverse_lazy('index')
    get_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):

        context = {

        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # form = self.form_class(request.POST, request.FILES)

        # if form.is_valid():
            
        #     return redirect(self.success_url)
        # else:
            
        #     return redirect(self.get_url)

        pass

