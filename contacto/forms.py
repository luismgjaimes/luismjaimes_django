from django import forms


class FormularioContacto(forms.Form):

    nombre=forms.CharField(label="Nombre", required=True)

    email=forms.CharField(label="EmailNombre", required=True)

    contenido=forms.CharField(label="Contenido")

