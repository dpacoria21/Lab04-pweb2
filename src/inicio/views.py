from urllib.request import HTTPHandler
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(request,*args, **kwargs):
    myContext = {
        'myText' : 'Esto es sobre nosotros',
        'myNumber' : 123,
        'myList' : [33, 44, 55],
        'mySecondList' : ['a','b','c','d','e']
    }
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", myContext)

def anotherView(request):
    print(request.user)
    return HttpResponse('<h1>Solo otra pagina</h1>')

def baseView(request, *args, **kwargs):
    return render(request, "base.html",{})

def mipageView(request,*args, **kwargs):
    return render(request, "tags.html",{})