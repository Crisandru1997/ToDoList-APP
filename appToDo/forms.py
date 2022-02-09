from dataclasses import field, fields
from django import forms
from .models import Proyecto, Tarea
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
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

class formularioRegistro(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Usuario', 'class': 'input-login', 'pattern':'[a-z]{1,9}', 'title':'El nombre de usuario debe tener de 1 a 9 caracteres.'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'Correo', 'class': 'input-login', 'type':'email'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'input-login'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar Contraseña', 'class': 'input-login'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1' ,'password2')
        # Con esto podemos eliminar los textos de ayuda.
        help_texts = {k:"" for k in fields}
        widgets = {
            'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
        }