from django.urls import path
from personas.views import *

app_name = 'auxiliar'

urlpatterns = {
    path('agregar/', personaCreateView, name ='adding'),
    path('<int:myID>/', personasShowObject, name='browsing'),
    path('<int:myID>/delete/', personasDeleteView, name='deleting'),
    path('', personasListView, name = 'listing'),
}