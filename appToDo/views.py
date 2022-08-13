import datetime
from tkinter.tix import Tree
from django.shortcuts import redirect, render
from pytz import timezone
from appToDo.forms import proyectoForm
from .models import Proyecto, Tarea
from .forms import proyectoForm, tareaFormGeneral, tareaFormProyecto, actualizarTarea
from django.shortcuts import get_object_or_404
from .forms import formularioRegistro
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    todos_los_proyectos = Proyecto.objects.filter(propietario=request.user)
    todas_las_tareas_hoy = Tarea.objects.filter(completado=False, propietario=request.user).order_by('id')
    tareas_completadas = Tarea.objects.filter(completado=True, propietario=request.user)
    form_nueva_tarea = nueva_tarea_general(request)
    form_nuevo_proyecto = nuevoProyecto(request)
    fecha_actual = datetime.date.today
    nueva_tarea = actualizar_tarea(request)
    return render(request, 'appToDo/listado_tareas.html', {'proyectos':todos_los_proyectos, 'tareas_hoy':todas_las_tareas_hoy, 'tareas_completadas':tareas_completadas, 'form_tarea':form_nueva_tarea, 'form_proyecto':form_nuevo_proyecto, 'fecha_actual':fecha_actual, 'nueva_tarea':nueva_tarea})

def nuevoProyecto(request):
    if request.method == 'POST':
        form = proyectoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            estado = verificarProyecto(post.titulo_proyecto, request.user)
            if estado:
                post.propietario = request.user
                post.save()
                form = proyectoForm()
            else:
                form = proyectoForm()
    else:
        form = proyectoForm()
    return form

def verificarProyecto(proyecto, user):
    p = Proyecto.objects.filter(titulo_proyecto=proyecto, propietario=user).exists()
    if p:
        return False
    else:
        return True

def verificar(request, proyecto):
    esta = get_object_or_404(Proyecto, propietario=request.user, titulo_proyecto=proyecto)
    if esta:
        return True
    else:
        return False

def proyecto_seleccionado(request, proyecto):
    esta = verificar(request, proyecto)
    fecha_actual = datetime.date.today
    if esta:
        # Seleccionamos el proyecto seleccionado.
        form_nuevo_proyecto = nuevoProyecto(request)
        proyectos = Proyecto.objects.filter(propietario=request.user)
        proyecto = get_object_or_404(Proyecto,propietario=request.user, titulo_proyecto=proyecto)
        # Generamos el formulario para ese proyecto en especifico.
        form = nueva_tarea_proyecto(request, proyecto)
        listado_tareas = Tarea.objects.filter(completado=False, titulo_proyecto=proyecto, propietario=request.user).order_by('id')
        tareas_completadas = Tarea.objects.filter(completado=True, titulo_proyecto=proyecto, propietario=request.user)
        nueva_tarea = actualizar_tarea(request)
        nuevo_nombre_proyecto = actualizar_proyecto(request)
        if nuevo_nombre_proyecto:
            return redirect('proyecto_seleccionado', proyecto=nuevo_nombre_proyecto)
        return render(request, 'appToDo/proyecto_individual.html', {'proyecto':proyecto, 'form':form, 'tareas':listado_tareas, 'tareas_completadas':tareas_completadas, 'proyectos':proyectos, 'form_proyecto':form_nuevo_proyecto, 'fecha_actual':fecha_actual, 'nueva_tarea':nueva_tarea, 'nuevo_proyecto':nuevo_nombre_proyecto})
    else:
        return render(request, 'appToDo/error.html', {})

# Se creara una nueva tarea segun el proyecto seleccionado.
def nueva_tarea_proyecto(request, proyecto):
    if request.method == 'POST':
        form = tareaFormProyecto(request.POST, request.user)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.titulo_proyecto = proyecto
            tarea.propietario = request.user
            tarea.save()
            #form = tareaFormGeneral()
    else:
        form = tareaFormProyecto()
    return form

# Se creara una tarea general, sin un proyecto especificado.
def nueva_tarea_general(request):
    if request.method == 'POST':
        form = tareaFormGeneral(request.user , request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.propietario = request.user
            tarea.save()
            form = tareaFormGeneral(request.user)
    else:
        form = tareaFormGeneral(request.user)
    return form

def completar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    tarea.completar()
    return redirect(request.META['HTTP_REFERER'])

def descompletar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    tarea.descompletar()
    return redirect(request.META['HTTP_REFERER'])

def registro(request):
    if request.method == 'POST':
        # Recibimos los datos del registro.
        form = formularioRegistro(request.POST)
        # Verificamos si los datos ingresados son validos.
        if form.is_valid():
            # Guardamos al nuevo usuario.
            form.save()
            # Enviamos el nombre de usuario al inicio.
            user = request.POST['username']
            nuevo_usuario = authenticate(username=request.POST['username'], password=request.POST['password1'])
            login(request, nuevo_usuario)
            proyectoDefault(nuevo_usuario)
            return redirect('inicio')
    else:
        form = formularioRegistro()
    return render(request, 'registration/registro.html', {'form':form})

# Proyecto creado por default.
def proyectoDefault(usuario):
    form = proyectoForm()
    post = form.save(commit=False)
    post.propietario = usuario
    post.titulo_proyecto = 'Todos'
    post.color = 'Gray'
    post.save()
    form = proyectoForm()
    return form

def eliminarTarea(request, pk):
    tarea = Tarea.objects.get(pk=pk)
    tarea.delete()
    return redirect(request.META['HTTP_REFERER'])

def eliminarProyecto(request, pk):
    proyecto = Proyecto.objects.get(pk=pk)
    proyecto.delete()
    return redirect(request.META['HTTP_REFERER'])

def eliminarProyectoIndividual(request, pk):
    proyecto = Proyecto.objects.get(pk=pk)
    proyecto.delete()
    return redirect('inicio')

def actualizar_tarea(request):
    id = request.POST.get('id')
    titulo = request.POST.get('titulo')
    if titulo != '':
        nuevo = Tarea.objects.filter(pk=id).update(titulo_tarea=titulo)
    else:
        nuevo = Tarea()
    return nuevo

def actualizar_proyecto(request):
    id = request.POST.get('id-proyecto')
    titulo = request.POST.get('titulo-proyecto')
    if titulo != '':
        proyecto = Proyecto.objects.filter(pk=id).update(titulo_proyecto=titulo)
    return titulo