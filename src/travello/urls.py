from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addDestination/<int:myID>', views.addDestination, name='addDestination'),
    path('listarDestinos', views.listarDestinos, name='listarDestinos'),
    path('modDestino/<int:myID>', views.modDestino, name='modDestino'),
    path('eliminarDestino/<int:myID>', views.eliminarDestino, name='eliminarDestino'),
]