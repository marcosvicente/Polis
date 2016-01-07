from django import forms

from .models import Usuario


class UsuarioForm(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    usuario = forms.CharField(max_length=100)
    dia = forms.IntegerField()
    mes = forms.CharField(max_length=100)
    ano = forms.IntegerField()
    senha = forms.CharField(max_length=100)
   
