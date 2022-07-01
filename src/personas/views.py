from django.shortcuts import render
from .models import Persona
from .forms import PersonaForm, RawPersonaForm

# Create your views here.
def personaTestView(request):
    obj = Persona.objects.get(id = 1)
    context ={
        'objeto': obj,
        }
    return render(request, 'personas/test.html', context)

def personaCreateView(request):
    print(request)
    if request.method == 'POST':
        nombre = request.POST.get('q')
        print(nombre)
    context = {}
    return render(request, 'personas/personasCreate.html', context)

def searchForHelp(request):
    return render(request, 'personas/search.html',{})

def personasAnotherCreateView(request):
    form = RawPersonaForm()
    if request.method == "POST":
       form = RawPersonaForm(request.POST)
       print('here!') 
    context = {
        'form':form,
    }
    print(form)
    return render(request, 'personas/personasCreate2.html', context)
