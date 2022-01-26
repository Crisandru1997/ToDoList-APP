from dataclasses import field, fields
from django import forms
from .models import Proyecto, Tarea
from django.forms.widgets import DateInput
import datetime

class proyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ('titulo_proyecto','color')
        widgets = {
            'color': forms.RadioSelect(choices=Proyecto.COLORES)   
        }
        
class tareaFormProyecto(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ('titulo_tarea', 'fecha_vencimiento')
        widgets = {
            'fecha_vencimiento': DateInput(attrs={'type': 'date'}),
        }

class tareaFormGeneral(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ('titulo_tarea', 'fecha_vencimiento', 'titulo_proyecto')
        widgets = {
            'fecha_vencimiento': DateInput(attrs={'type': 'date'}),
        }
