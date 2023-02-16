from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def indicadores_index(request):
    return HttpResponse("Hola aqui estan los indicadores")