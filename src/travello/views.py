from gc import get_objects
from imp import reload
from unicodedata import name
from django.shortcuts import render, redirect, get_object_or_404
from .models import Destination
from .forms import DestinationForm
# Create your views here.

def addDestination(request, myID):
    form = DestinationForm(request.POST, request.FILES)
    
    if form.is_valid():
        form.save()
        form = DestinationForm()
        return redirect('/listarDestinos')
    else:
        form = DestinationForm()
    context = {
        'form' : form
    }
    
    return render(request, 'addDestination.html',context)

def listarDestinos(request):
    dests = Destination.objects.all()
    return render(request, 'listarDestinos.html', {'Destin': dests})

def index(request):

    dests = Destination.objects.all()

    return render(request, 'index.html',{'Destin': dests})

def modDestino(request, myID):
    obj = Destination.objects.get(id=myID)
    if request.method == 'POST':
        print('entro de una aqui senito')
        form = DestinationForm(request.POST,request.FILES,instance=obj)
        if form.is_valid():
            form.save()
            form = DestinationForm()
            return redirect('/listarDestinos')
    else:
        print('here')
        form = DestinationForm(request.POST or None,instance=obj)
    context = {
        'form': form,
    }
    return render(request, 'modDestino.html',context)

def eliminarDestino(request, myID):
    obj = Destination.objects.get(id = myID)
    if request.method == 'POST':
        obj= get_object_or_404(Destination, id=myID)
        print("Lo borro")
        obj.delete()
        return redirect('/listarDestinos')
    context = {
        'dest' : obj
    }
    return render(request, 'eliminarDestino.html', context)
