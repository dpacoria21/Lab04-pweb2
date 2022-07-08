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
    PersonaDetailView,
    PersonaCreateView,
    PersonaUpdateView,
    PersonaDeleteView,
)

app_name = 'auxiliar'

urlpatterns = [
    path('anotherAdd/', personasAnotherCreateView, name='otroAgregarPersona'),
    path('persona/', personaTestView, name='testViewPersona'),
    #path('agregar/', personaCreateView, name ='adding'),
    # path('<int:myID>/', personasShowObject, name='browsing'),
    # path('<int:myID>/delete/', personasDeleteView, name='deleting'),
    # path('', personasListView, name = 'listing'),
    path('search/', searchForHelp, name='buscar'),
    path('', PersonaListView.as_view(), name='persona-list'),
    path('<int:pk>/', PersonaDetailView.as_view(), name='persona-detail'),
    path('create/', PersonaCreateView.as_view(), name = 'persona-create'),
    path('<int:pk>/update/', PersonaUpdateView.as_view(), name="persona-update"),
    path('<int:pk>/delete/', PersonaDeleteView.as_view(), name='persona-delete'),
]
