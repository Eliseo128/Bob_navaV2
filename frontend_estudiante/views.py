from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Estudiante
from .forms import EstudianteForm

# Create your views here.
def index(request):
    return render(request, 'frontend_estudiante/index.html',{'estudiantes': Estudiante.objects.all()    })


def ver_estudiante(request, id):
   
    return HttpResponseRedirect(reverse('index')) 

def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            nuevo_num_estudiante = form.cleaned_data['num_estudiante']
            nuevo_nombre = form.cleaned_data['nombre']
            nuevo_apellido = form.cleaned_data['apellido']
            nuevo_email = form.cleaned_data['email']
            nuevo_area_estudio = form.cleaned_data['area_estudio']
            nuevo_gpa = form.cleaned_data['gpa']

            nuevo_estudiante= Estudiante(
                num_estudiante=nuevo_num_estudiante,
                nombre=nuevo_nombre,
                apellido=nuevo_apellido,
                email=nuevo_email,
                area_estudio=nuevo_area_estudio,
                gpa=nuevo_gpa
            )
            nuevo_estudiante.save()

            return render(request, 'frontend_estudiante/crear_estudiante.html', {
                'form': EstudianteForm(),
                'success': True
            
            })
        else:
            form = EstudianteForm()
    return render(request, 'frontend_estudiante/crear_estudiante.html', {       
        'form': EstudianteForm()
        
    })


def editar_estudiante(request, id):

    if request.method == 'POST':
        estudiante = Estudiante.objects.get(id=id)


        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return render(request, 'frontend_estudiante/editar_estudiante.html', {
                'form': EstudianteForm(instance=estudiante),
                'success': True
            })
    else:
        estudiante = Estudiante.objects.get(id=id)
        form = EstudianteForm(instance=estudiante)
    return render(request, 'frontend_estudiante/editar_estudiante.html', {
        'form': form
    })

def eliminar_estudiante(request, id):
    if request.method == 'POST':
        estudiante = Estudiante.objects.get(id=id)
        estudiante.delete()
        return HttpResponseRedirect(reverse('index'))
    