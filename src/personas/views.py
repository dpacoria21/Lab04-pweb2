from dataclasses import fields
from http.client import HTTPResponse
from django.http import HttpResponse
from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from .models import Persona
from .forms import PersonaForm, RawPersonaForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    View,
)
from django.urls import reverse_lazy
from django.http import JsonResponse

# Create your views here.

class PersonaListView(ListView):
    model = Persona
    
class PersonaDetailView(DetailView):
    model = Persona

class PersonaCreateView(CreateView):
    model = Persona
    fields = [
        'nombre',
        'apellidos',
        'edad',
        'donador',
    ]

class PersonaUpdateView(UpdateView):
    model = Persona
    fields = [
        'nombre',
        'apellidos',
        'edad',
        'donador',
    ]

class PersonaDeleteView(DeleteView):
    model = Persona
    success_url = reverse_lazy('auxiliar:persona-list')

class PersonaQueryView(View):
    def get(self, request, *args, **kwargs):
        queryset = Persona.objects.filter(edad__lte='40')
        return JsonResponse(list(queryset.values()), safe=False)

def personaTestView(request):
    obj = Persona.objects.get(id = 1)
    context ={
        'objeto': obj,
        }
    return render(request, 'personas/test.html', context)

def personaCreateView(request):
    initialValues = {
        'nombre' : 'Sin nombre',
    }
    form = PersonaForm(request.POST or None, initial = initialValues)
    if form.is_valid():
        form.save()
        form = PersonaForm()
    context = {
        'form': form,
    }
    return render(request, 'personas/personasCreate.html', context)

def searchForHelp(request):
    return render(request, 'personas/search.html',{})

def personasAnotherCreateView(request):
    form = RawPersonaForm()
    if request.method == "POST":
       form = RawPersonaForm(request.POST)
       if form.is_valid():
        print(form.cleaned_data)
        Persona.objects.create(**form.cleaned_data)
       else:
        print(form.errors)
    context = {
        'form':form,
    }
    return render(request, 'personas/personasCreate2.html', context)

def personasShowObject(request, myID):
    obj = get_object_or_404(Persona, id=myID)
    context = {
        'objeto' : obj,
    }
    return render(request, 'personas/descripcion.html', context)

def personasDeleteView(request, myID):
    obj = get_object_or_404(Persona, id=myID)
    if request.method == 'POST':
        print('Lo borro ahora')
        obj.delete()
        return redirect('../../../miPagina/')
    context = {
        'objeto': obj,
    }
    return render(request, 'personas/personasBorrar.html', context)
def personasListView(request):
    queryset = Persona.objects.all()
    context = {
        'objectList' : queryset,
    }
    return render(request, 'personas/personasLista.html',context)
