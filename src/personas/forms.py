from tkinter import Widget
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
    nombre = forms.CharField(
        widget = forms.Textarea(
            attrs={
                'placeholder' : 'Solo tu nombre, por favor',
                'id' : 'nombreID',
                'class': 'especial',
                'cols' : '10',
            }
        )
    )
    apellidos = forms.CharField()
    edad = forms.IntegerField(initial=20)
    donador = forms.BooleanField()
    def clean_nombre(self, *args, **kwargs):
        print('paso')
        name = self.cleaned_data.get('nombre')
        if name.istitle():
            return name
        else:
            raise forms.ValidationError('La primera letra en mayuscula')
    