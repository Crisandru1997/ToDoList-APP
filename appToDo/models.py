from operator import mod
from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
import datetime

class Proyecto(models.Model):
    COLORES= [
    ('red', 'red'),
    ('blue', 'blue'),
    ('green', 'green'),
    ('orange', 'orange'),
    ]
    titulo_proyecto = models.CharField(max_length=20)
    color = models.CharField(choices=COLORES, default=None, max_length=20)
    
    def __str__(self):
        return self.titulo_proyecto 

class Tarea(models.Model):
    titulo_tarea = models.CharField(max_length=80)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_vencimiento = models.DateField(blank=True, validators=[MinValueValidator(datetime.date.today)])
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

