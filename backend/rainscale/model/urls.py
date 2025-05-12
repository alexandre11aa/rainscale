from django.urls import path

from model.views.model import (
    IndexView,
    MapaView,
    SobreView,
    TutorialView
)

urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('index/', IndexView.as_view(), name='index'),
    path('mapa/', MapaView.as_view(), name='mapa'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('tutorial/', TutorialView.as_view(), name='tutorial')

]
