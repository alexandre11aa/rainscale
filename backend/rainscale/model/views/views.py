# from .forms import EnderecoForm, EnderecoSearchForm, LocalForm
# from .models import Endereco, Local
# from colaboradores.utils import separador_de_erros, primeiro_nome

# from django.views import View
# from django.urls import reverse_lazy
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator

# from django.db.models import Q

# ## CRUD Endereço

# @method_decorator(login_required, name='dispatch')
# class EnderecoRegisterView(View):
#     form_class = EnderecoForm
#     template_name = '../templates/endereco/endereco_register.html'
#     success_url = reverse_lazy('list_endereco')
#     get_url = reverse_lazy('register_endereco')

#     def get(self, request, *args, **kwargs):
#         # Formulário vazio para um novo registro
#         form = self.form_class()
#         notification = request.session.pop('notification', None)
#         context = {
#             'form': form,
#             'notification': notification,
#             'nome_colaborador': primeiro_nome(request.user.nome_colaborador)
#         }
#         return render(request, self.template_name, context)

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST, request.FILES)

#         if form.is_valid():
#             form.save()
#             # Armazena o contexto na sessão
#             request.session['notification'] = {
#                 'message': 'Endereço registrado com sucesso!',
#                 'title': 'Sucesso',
#                 'icon': 'success'
#             }
#             return redirect(self.success_url)
#         else:
#             erros = separador_de_erros(form.errors)            
#             # Notificação de erro
#             request.session['notification'] = {
#                 'message': erros,
#                 'title': 'Erro',
#                 'icon': 'error'
#             }
#             return redirect(self.get_url)

# @method_decorator(login_required, name='dispatch')
# class EnderecoUpdateView(View):
#     form_class = EnderecoForm
#     template_name = '../templates/endereco/endereco_register.html'
#     success_url = reverse_lazy('list_endereco')

#     def get_object(self):
#         # Tenta pegar o objeto pelo ID nos parâmetros. Se não encontrar, retorna 404.
#         id = self.kwargs.get('id')
    
#         if id:
#             try:
#                 return Endereco.all_objects.get(id=id)
#             except:
#                 return None

#         return None

#     def get(self, request, *args, **kwargs):
#         endereco = self.get_object()

#         if endereco:
#             form = self.form_class(instance=endereco)  
#         else:
#             return redirect('register_endereco')
        
#         notification = request.session.pop('notification', None)
#         context = {
#             'form': form,
#             'notification': notification,
#             'nome_colaborador': primeiro_nome(request.user.nome_colaborador)
#         }
#         return render(request, self.template_name, context)

#     def post(self, request, *args, **kwargs):
#         endereco = self.get_object()

#         if endereco:
#             form = self.form_class(request.POST, request.FILES, instance=endereco)
        
#         else:
#             form = self.form_class(request.POST, request.FILES)

#         if form.is_valid():
#             form.save()
#             # Armazena o contexto na sessão
#             request.session['notification'] = {
#                 'message': 'Endereço atualizado com sucesso!',
#                 'title': 'Sucesso',
#                 'icon': 'success'
#             }
#             return redirect(self.success_url)
#         else:
#             erros = separador_de_erros(form.errors)            
#             # Notificação de erro
#             request.session['notification'] = {
#                 'message': erros,
#                 'title': 'Erro',
#                 'icon': 'error'
#             }
#             return redirect('update_endereco', id=endereco.id)

# @method_decorator(login_required, name='dispatch')
# class EnderecoListView(View):
#     model = Endereco
#     template_name = '../templates/endereco/endereco_list.html'

#     def get(self, request, *args, **kwargs):
        
#         # Busca todos os endereco do banco de dados
#         endereco = self.model.all_objects.all()

#         busca_form = EnderecoSearchForm(request.GET or None)

#         notification = request.session.pop('notification', None)

#         context = {
#             'form': endereco,
#             'busca_form': busca_form,
#             'notification': notification,
#             'nome_colaborador': primeiro_nome(request.user.nome_colaborador)
#         }

#         return render(request, self.template_name, context)
    
#     def post(self, request, *args, **kwargs):
#         form = EnderecoSearchForm(request.POST or None)  # Mantenha o formulário preenchido após a pesquisa

#         enderecos = Endereco.all_objects.all()

#         # Verifique os erros do formulário
#         if form.is_valid():
#             logradouro = form.cleaned_data.get('logradouro')
#             numero = form.cleaned_data.get('numero')
#             bairro = form.cleaned_data.get('bairro')
#             nome_municipio = form.cleaned_data.get('nome_municipio')
#             uf = form.cleaned_data.get('uf')
#             is_active = form.cleaned_data.get('is_active')

#             # Gera filtro vazio
#             filtros = Q()

#             # Filtra pelo logradouro, se fornecido
#             if logradouro:
#                 filtros &= Q(logradouro__icontains=logradouro)

#             # Filtra pelo número, se fornecido
#             if numero:
#                 filtros &= Q(numero__icontains=numero)

#             # Filtra pelo bairro, se fornecido
#             if bairro:
#                 filtros &= Q(bairro__icontains=bairro)

#             # Filtra pelo município, se fornecido
#             if nome_municipio:
#                 filtros &= Q(nome_municipio__icontains=nome_municipio)

#             # Filtra pela UF, se fornecido
#             if uf:
#                 filtros &= Q(uf__icontains=uf)

#             # Filtra pelo status de ativo, se fornecido
#             if is_active == 'A':
#                 filtros &= Q(is_active=True)
#             elif is_active == 'I':
#                 filtros &= Q(is_active=False)

#             # Aplica filtros
#             enderecos = enderecos.filter(filtros).distinct()

#         context = {
#             'form': enderecos,
#             'busca_form': form,
#             'nome_colaborador': primeiro_nome(request.user.nome_colaborador)
#         }

#         return render(request, self.template_name, context)
    
# @method_decorator(login_required, name='dispatch')
# class EnderecoDeleteView(View):
#     model = Endereco
#     template_name = '../templates/endereco/endereco_list.html'

#     def post(self, request, *args, **kwargs):

#         # Obtém o objeto endereco ou retorna 404 se não existir
#         endereco = get_object_or_404(self.model.all_objects.all(), id=request.POST.get("endereco_id"))

#         # Obtém o valor do campo `ativar_desativar` do formulário
#         ativar_desativar = request.POST.get("ativar_desativar")

#         # Lógica para soft delete e restore
#         if ativar_desativar == "True":
#             # "Ativar" o endereco
#             endereco.recover()
#             message = f'Endereço {endereco} ativado com sucesso!'
#         else:
#             # "Inativar" o endereco
#             endereco.soft_delete()
#             message = f'Endereço {endereco} inativado com sucesso!'

#         # Armazena o contexto na sessão
#         request.session['notification'] = {
#             'message': message,
#             'title': 'Sucesso',
#             'icon': 'success'
#         }

#         # Redireciona para a lista de enderecos após a atualização
#         return redirect('list_endereco')
