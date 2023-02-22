from django.contrib import admin
from django.urls import path
from Apps.usuario import views
import re


app_name = 'usuario'

urlpatterns = [
    path('registrar/',views.RegisroUsuario.as_view(), name='registrar'),

]