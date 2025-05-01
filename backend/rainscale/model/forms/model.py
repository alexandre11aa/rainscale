from django import forms
from django.db import transaction


class IndexForm(forms.Form):

    latitude = forms.CharField(
        label='Latitude',
        max_length=50,
        required=True,
        error_messages={
            'max_length': 'O campo Número ultrapassou o limite de caracteres.',
            'required': '',
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Número',
        })
    )

    longitude = forms.CharField(
        label='Complemento',
        max_length=50,
        required=True,
        error_messages={
            'max_length': 'O campo Número ultrapassou o limite de caracteres.',
            'required': '',
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Número',
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        campos_vazios(cleaned_data, self.fields)
        return cleaned_data

    @transaction.atomic
    def save(self, dados):
    
        print('OI')

        return 'OI'