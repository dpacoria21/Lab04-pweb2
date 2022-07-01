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
    nombre = forms.CharField()
    apellidos = forms.CharField()
    edad = forms.IntegerField()
    donador = forms.BooleanField()