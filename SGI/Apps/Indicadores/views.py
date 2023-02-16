from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def indicadores_index(request):
    return render(request,'indicadores/index.html')

def base(request):
    return render(request,'base/base.html')    