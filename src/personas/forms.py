from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'nombre',
            'apellidos',
            'edad',
            'donador',
        ]

class RawPersonaForm(forms.Form):
    nombre = forms.CharField(label='Your name')
    apellidos = forms.CharField()
    edad = forms.IntegerField(initial=20)
    donador = forms.BooleanField()