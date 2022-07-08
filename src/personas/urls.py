from django.urls import path
from personas.views import (
    personaTestView,
    personasShowObject,
    personasDeleteView,
    personaCreateView,
    personasListView,
    personasAnotherCreateView,
    searchForHelp
)
from .views import (
    PersonaListView,
)

app_name = 'auxiliar'

urlpatterns = [
    path('anotherAdd/', personasAnotherCreateView, name='otroAgregarPersona'),
    path('persona/', personaTestView, name='testViewPersona'),
    path('agregar/', personaCreateView, name ='adding'),
    path('<int:myID>/', personasShowObject, name='browsing'),
    path('<int:myID>/delete/', personasDeleteView, name='deleting'),
    path('', personasListView, name = 'listing'),
    path('search/', searchForHelp, name='buscar'),
    path('listar', PersonaListView.as_view(), name='persona-list'),
]