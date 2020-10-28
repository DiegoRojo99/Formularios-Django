from django import forms

class EmpleadoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=40)
    apellidos = forms.CharField(label="Apellidos", max_length=150)
    email = forms.EmailField(label="Email", required=False)
    direccion = forms.CharField(label="Direccion")
    edad = forms.IntegerField(label="Edad")