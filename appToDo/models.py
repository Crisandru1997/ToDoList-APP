from math import fabs
from operator import mod
from django.db import models
from django.core.validators import MinValueValidator
# from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
import datetime

class Proyecto(models.Model):
    COLORES= [
    ('red', 'red'),
    ('blue', 'blue'),
    ('green', 'green'),
    ('orange', 'orange'),
    ('gray', 'gray')
    ]
    titulo_proyecto = models.CharField(max_length=20, null=False)
    propietario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    color = models.CharField(choices=COLORES, default=None, max_length=20)
    
    def __str__(self):
        return self.titulo_proyecto 

class Tarea(models.Model):
    propietario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False)
    titulo_tarea = models.CharField(max_length=80, null=False, blank=False)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_vencimiento = models.DateField(blank=True, null=True, validators=[MinValueValidator(datetime.date.today)])
    completado = models.BooleanField(default=False)
    titulo_proyecto = models.ForeignKey(Proyecto, 
                                        on_delete=models.CASCADE, 
                                        null=False, # No puede ser nulo. 
                                        blank=False,# No debe almacenar valores vacios.
                                        default='Todos') 
    def __str__(self):
        return self.titulo_tarea
    def completar(self):
        self.completado = True
        self.save()
    def descompletar(self):
        self.completado = False
        self.save()

