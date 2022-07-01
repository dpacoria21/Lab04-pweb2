"""listaContactos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio.views import myHomeView
from inicio.views import anotherView
from inicio.views import mipageView
from inicio.views import baseView
from personas.views import personaTestView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myHomeView, name='Pagina de Inicio'),
    path('another/', anotherView, name='Otra pagina'),
    path('miPagina/', mipageView, name='Uso de tags'),
    path('paginaBase/', baseView, name='Pagina Base'),
    path('persona/', personaTestView, name='otro'),
]
