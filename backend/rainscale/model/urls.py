from django.urls import path
from model.views.model import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index')
]
