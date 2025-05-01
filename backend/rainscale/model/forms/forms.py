# from django import forms
# from django.db import transaction

# from setor.choices import STATUS_CHOICES
# from .models import Endereco, Local
# from colaboradores.validations import campos_vazios


# class EnderecoForm(forms.Form):
#     logradouro = forms.CharField(
#         label='Logradouro',
#         max_length=255,
#         required=True,
#         error_messages={
#             'max_length': 'O campo Endereço ultrapassou o limite de caracteres.',
#             'required': '',
#         },
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Logradouro',
#             'id':'rua',
#         })
#     )
    
#     numero = forms.CharField(
#         label='Número',
#         max_length=50,
#         required=True,
#         error_messages={
#             'max_length': 'O campo Número ultrapassou o limite de caracteres.',
#             'required': '',
#         },
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Número',
#         })
#     )

#     complemento = forms.CharField(
#         label='Complemento',
#         max_length=255,
#         required=False,
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Complemento',
#         })
#     )

#     bairro = forms.CharField(
#         label='Bairro',
#         max_length=255,
#         required=True,
#         error_messages={
#             'max_length': 'O campo Bairro ultrapassou o limite de caracteres.',
#             'required': '',
#         },
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Bairro',
#             'id':'bairro',
#         })
#     )

#     '''
#     codigo_municipio = forms.CharField(
#         label='Código do Município',
#         max_length=20,
#         required=True,
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Código do Município',
#         })
#     )
#     '''

#     cep = forms.CharField(
#         label='CEP',
#         max_length=10,
#         required=True,
#         error_messages={
#             'max_length': 'O campo CEP ultrapassou o limite de caracteres.',
#             'required': '',
#         },
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'CEP',
#             'id':'cep',
#         })
#     )

#     nome_municipio = forms.CharField(
#         label='Nome do Município',
#         max_length=255,
#         required=True,
#         error_messages={
#             'max_length': 'O campo Nome Município ultrapassou o limite de caracteres.',
#             'required': '',
#         },
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Nome do Município',
#             'id':'cidade',
#         })
#     )

#     uf = forms.CharField(
#         label='UF',
#         max_length=2,
#         required=True,
#         error_messages={
#             'max_length': 'O campo UF ultrapassou o limite de caracteres.',
#             'required': '',
#         },
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'UF',
#             'id':'uf',
#         })
#     )

#     nome_municipio_estrangeiro = forms.CharField(
#         label='Nome do Município Estrangeiro',
#         max_length=255,
#         required=False,
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Nome do Município Estrangeiro',
#         })
#     )

#     def __init__(self, *args, **kwargs):

#         # Aceitamos a instância do modelo 'Campus' como argumento opcional
#         self.instance = kwargs.pop('instance', None)
#         super().__init__(*args, **kwargs)

#         # Se uma instância for passada, populamos o formulário com seus valores
#         if self.instance:
#             self.fields['logradouro'].initial = self.instance.logradouro
#             self.fields['numero'].initial = self.instance.numero
#             self.fields['complemento'].initial = self.instance.complemento
#             self.fields['bairro'].initial = self.instance.bairro
#             self.fields['cep'].initial = self.instance.cep
#             self.fields['nome_municipio'].initial = self.instance.nome_municipio
#             self.fields['uf'].initial = self.instance.uf
#             self.fields['nome_municipio_estrangeiro'].initial = self.instance.nome_municipio_estrangeiro

#     def clean(self):
#         cleaned_data = super().clean()
#         campos_vazios(cleaned_data, self.fields)
#         return cleaned_data

#     @transaction.atomic
#     def save(self, commit=True):
    
#         # Se já houver uma instância, apenas atualize os dados da mesma
#         endereco = self.instance if self.instance else Endereco()

#         # Atualizando os campos do colaborador
#         endereco.logradouro = self.cleaned_data['logradouro'].upper()
#         endereco.numero = self.cleaned_data['numero'].upper()
#         endereco.complemento = self.cleaned_data['complemento'].upper()
#         endereco.bairro = self.cleaned_data['bairro'].upper()
#         endereco.cep = self.cleaned_data['cep'].upper()
#         endereco.nome_municipio = self.cleaned_data['nome_municipio'].upper()
#         endereco.uf = self.cleaned_data['uf'].upper()
#         endereco.nome_municipio_estrangeiro = self.cleaned_data['nome_municipio_estrangeiro'].upper()

#         # Salvando a instância no banco de dados
#         if commit:
#             endereco.save()

#         return endereco
    

# class EnderecoSearchForm(forms.Form):
#     logradouro = forms.CharField(
#         label='Logradouro',
#         max_length=255,
#         required=False,
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Logradouro',
#         })
#     )
    
#     numero = forms.CharField(
#         label='Número',
#         max_length=50,
#         required=False,
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Número',
#         })
#     )

#     bairro = forms.CharField(
#         label='Bairro',
#         max_length=255,
#         required=False,
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Bairro',
#         })
#     )

#     nome_municipio = forms.CharField(
#         label='Nome do Município',
#         max_length=255,
#         required=False,
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Nome do Município',
#         })
#     )

#     uf = forms.CharField(
#         label='UF',
#         max_length=2,
#         required=False,
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'UF',
#         })
#     )
    
#     is_active = forms.ChoiceField(
#         choices=STATUS_CHOICES,
#         required=True,
#         label="Status",
#         widget=forms.Select(attrs={
#             'class': 'form-select',
#         }),
#     )