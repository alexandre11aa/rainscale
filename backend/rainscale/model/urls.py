from django.urls import path

from model.views.model import (
    IndexView,
    SobreView,
    TutorialView
)

urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('index/', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('tutorial/', TutorialView.as_view(), name='tutorial')

]
