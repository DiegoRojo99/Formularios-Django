from django.http import HttpResponse
from django.shortcuts import render

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