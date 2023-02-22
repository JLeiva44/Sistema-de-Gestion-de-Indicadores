from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from Apps.usuario.forms import RegistroForm


# Create your views here.

class RegisroUsuario(CreateView):
    model = User
    template_name: str = 'usuario/registrar.html'
    form_class = RegistroForm
    success_url = reverse_lazy('indicadores:listar_indicador')
