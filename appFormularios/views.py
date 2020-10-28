from django.http import HttpResponse
from django.shortcuts import render
from .forms import EmpleadoForm

# Create your views here.
def show_form(request):
    return render(request, 'registro.html')

def post_form(request):
    usuario = request.POST["usuario"]
    apellidos = request.POST["apellidos"]
    email = request.POST["email"]
    edad = request.POST["edad"]
    direccion = request.POST["direccion"]
    return HttpResponse(f"El usuario es {usuario} {apellidos}, tiene {edad} anyos, vive en {direccion} y su email es {email}")

def show_empleado_form(request):
    form = EmpleadoForm()
    return render(request, 'empleado_form.html', {'form':form})

def post_empleado_form(request):
    form = EmpleadoForm(request.POST)
    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']
        return HttpResponse(f"El nombre es {nombre} {apellidos}")
