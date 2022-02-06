from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.index), name='index'),
    path('<str:proyecto>', login_required(views.proyecto_seleccionado), name='proyecto_seleccionado'),
    path('<int:pk>/completar', login_required(views.completar_tarea), name='completar_tarea'),
    path('<int:pk>/descompletar', login_required(views.descompletar_tarea), name='descompletar_tarea'),
]