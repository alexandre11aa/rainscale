from django.urls import path

from model.views.index import IndexView
from model.views.mapa import MapaView
from model.views.sobre import SobreView
from model.views.tutorial import TutorialView


urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('index/', IndexView.as_view(), name='index'),
    path('mapa/<int:model_id>', MapaView.as_view(), name='mapa'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('tutorial/', TutorialView.as_view(), name='tutorial')

]
