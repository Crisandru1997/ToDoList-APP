from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.index), name='inicio'),
    path('<str:proyecto>/', login_required(views.proyecto_seleccionado), name='proyecto_seleccionado'),
    path('<int:pk>/completar', login_required(views.completar_tarea), name='completar_tarea'),
    path('<int:pk>/descompletar', login_required(views.descompletar_tarea), name='descompletar_tarea'),
    path('<int:pk>/eliminar-tarea', login_required(views.eliminarTarea), name='borrar_tarea'),
    path('<int:pk>/eliminar-proyecto', login_required(views.eliminarProyecto), name='borrar_proyecto'),
    path('<int:pk>/eliminar-proyecto-individual', login_required(views.eliminarProyectoIndividual), name='borrar_proyecto_individual'),
]