from django.shortcuts import redirect, render
from django.http import HttpResponse
from Apps.Indicadores.form import Indicador_Form
# Create your views here.

def indicadores_index(request):
    return render(request,'indicadores/index.html')


def indicadores_form(request):
    if request.method == 'POST':
        form =  Indicador_Form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Indicadores:index')    
    else:
        form = Indicador_Form()   
    return render(request,'indicadores/indicadores_form.html', {'form':form})     

def base(request):
    return render(request,'base/base.html')    