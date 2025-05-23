from django import forms
from django.db import transaction
from django.core.exceptions import ValidationError

class MapaForm(forms.Form):

    latitude = forms.DecimalField(
        label='Latitude',
        max_digits=10,
        decimal_places=6,
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Informe uma latitude...',
            'aria-label': 'Latitude',
            'aria-describedby': 'lat',
            'id': 'latitude'
        })
    )

    longitude = forms.DecimalField(
        label='Longitude',
        max_digits=10,
        decimal_places=6,
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Informe uma longitude...',
            'aria-label': 'Longitude',
            'aria-describedby': 'lon',
            'id': 'longitude'
        })
    )

    def clean_latitude(self):
        lat = self.cleaned_data['latitude']
        if lat < -90 or lat > 90:
            raise ValidationError("A latitude deve estar entre -90 e 90 graus.")
        return lat

    def clean_longitude(self):
        lon = self.cleaned_data['longitude']
        if lon < -180 or lon > 180:
            raise ValidationError("A longitude deve estar entre -180 e 180 graus.")
        return lon

    @transaction.atomic
    def get(self, request):

        latitude = self.cleaned_data['latitude']

        longitude = self.cleaned_data['longitude']

        return latitude, longitude
