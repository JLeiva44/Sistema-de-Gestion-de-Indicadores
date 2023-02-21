from re import L
from django.shortcuts import redirect, render
from django.http import HttpResponse
from Apps.Indicadores.form import Alarma_Form, Valor_Indicador_Form, Medida_Form,Indicador_Form
from Apps.Indicadores.models import Indicador
# Create your views here.

def indicadores_index(request):
    return render(request,'indicadores/index.html')

def indicador_list(request):
    indicador = Indicador.objects.all()
    contexto = {'indicadores' : indicador}
    return render(request,'indicadores/indicador_list.html', contexto)

def indicator_update(request, id_indicador):
    indicador = Indicador.objects.get(id = id_indicador)
    if request.method == 'GET':
        form = Indicador_Form(instance=indicador)
    else:
        form = Indicador_Form(request.POST, instance=indicador)
        if form.is_valid():
            form.save()    
        return redirect('indicadores:listar_indicador') 
    return render(request, 'indicadores/indicador_form.html', {'form':form} )       

def indicator_delete(request, id_indicador):
    indicador = Indicador.objects.get(id = id_indicador)
    if request.method == 'POST':
        indicador.delete()
        return redirect('indicadores:listar_indicador')
    return render(request, 'indicadores/indicador_delete.html', {'indicador':indicador} )       



def alarma_form(request):
    if request.method == 'POST':
        form =  Alarma_Form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Indicadores:index')    
    else:
        form = Alarma_Form()   
    return render(request,'indicadores/alarma_form.html', {'form':form})     

def valor_indicador_form(request):
    if request.method == 'POST':
        form =  Valor_Indicador_Form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')    
    else:
        form = Valor_Indicador_Form()   
    return render(request,'indicadores/valor_indicador_form.html', {'form':form})     

def medida_form(request):
    if request.method == 'POST':
        form =  Medida_Form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Indicadores:index')    
    else:
        form = Medida_Form()   
    return render(request,'indicadores/medida_form.html', {'form':form})     


def indicadores_form(request):
    if request.method == 'POST':
        form =  Indicador_Form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('indicadores:listar_indicador')    
    else:
        form = Indicador_Form()   
    return render(request,'indicadores/indicador_form.html', {'form':form})     

def base(request):
    return render(request,'base/base.html')    