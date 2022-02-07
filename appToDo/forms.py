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
            'color': forms.RadioSelect(choices=Proyecto.COLORES, attrs={
                'class': 'seleccion-color'    
            }),
            'titulo_proyecto': DateInput(attrs={
                'class': 'input-agregar-proyecto',
                'placeholder':'Añadir proyecto...',
                }
            ),
        }
        
class tareaFormProyecto(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ('titulo_tarea', 'fecha_vencimiento')
        widgets = {
            'fecha_vencimiento': DateInput(attrs={
                'type': 'date',
                'class': 'input-fecha-vencimiento',
                }
            ),
            'titulo_tarea': forms.TextInput(
                attrs={
                    'class': 'input-agregar-tarea',
                    'placeholder':'Añadir tarea...',
                }
            ),
        }

class tareaFormGeneral(forms.ModelForm):
    def __init__(self,usuario,*args,**kwargs):
        super (tareaFormGeneral,self ).__init__(*args,**kwargs) # populates the post
        self.fields['titulo_proyecto'].queryset = Proyecto.objects.filter(propietario=usuario)
        
    class Meta:
        model = Tarea
        fields = ('titulo_tarea', 'fecha_vencimiento', 'titulo_proyecto')
        widgets = {
            'fecha_vencimiento': DateInput(attrs={
                'type': 'date',
                'class': 'input-fecha-vencimiento',
                }
            ),
            'titulo_tarea': forms.TextInput(
                attrs={
                    'class': 'input-agregar-tarea',
                    'placeholder':'Añadir tarea...',
                }
            ),
            'titulo_proyecto': forms.Select(
                attrs={
                    'class': 'input-seleccion-proyecto',
                }
            ),
        }
