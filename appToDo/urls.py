from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:proyecto>', views.proyecto_seleccionado, name='proyecto_seleccionado'),
    path('<int:pk>/completar', views.completar_tarea, name='completar_tarea'),
    path('<int:pk>/descompletar', views.descompletar_tarea, name='descompletar_tarea'),
]