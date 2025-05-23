from django import forms
from django.db import transaction
from django.shortcuts import get_object_or_404

from model.models import Model
from model.validations import (
    lat_limit,
    lon_limit
)


class MapaForm(forms.Form):

    def __init__(self, *args, model_id=None, **kwargs):

        super().__init__(*args, **kwargs)

        self.model_id = model_id

        if self.model_id:
            self.model = get_object_or_404(Model, id=model_id)

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

        if self.model_id:
            lat_limit(
                lat,
                self.model.lat_maxima,
                self.model.lat_minima
            )
        else:
            lat_limit(lat)

        return lat

    def clean_longitude(self):
        lon = self.cleaned_data['longitude']

        if self.model_id:
            lon_limit(
                lon,
                self.model.lon_maxima,
                self.model.lon_minima
            )
        else:
            lon_limit(lon)

        return lon
    
    @transaction.atomic
    def get(self):

        latitude = self.cleaned_data['latitude']
        longitude = self.cleaned_data['longitude']

        return latitude, longitude
