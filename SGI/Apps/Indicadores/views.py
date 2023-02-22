from re import L
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from Apps.Indicadores.form import Alarma_Form, Valor_Indicador_Form, Medida_Form,Indicador_Form
from Apps.Indicadores.models import Indicador,Valor_Indicador, Alarma, Medida
# Create your views here.

# vistas basadas en clases

# Indicador..........
class Indicador_List(ListView):
    model = Indicador
    template_name: str = 'indicadores/indicador_list.html'

class Indicador_Create(CreateView):
    model = Indicador
    form_class= Indicador_Form
    template_name: str = 'indicadores/indicador_form.html'
    success_url= reverse_lazy('indicadores:listar_indicador')

class Indicador_Update(UpdateView):
    model = Indicador
    fields = '__all__'
    form_class = Indicador_Form
    template_name: str = 'indicadores/indicador_form.html'
    success_url = reverse_lazy('indicadores:listar_indicador')


class Indicador_Delete(DeleteView):
    model = Indicador
    fields = '__all__'   
    template_name: str = 'indicadores/indicador_delete.html'
    success_url = reverse_lazy('indicadores:listar_indicador')



# Valor Indicador
class Valor_Indicador_List(ListView):
    model = Valor_Indicador
    template_name: str = 'indicadores/valor_indicador/valor_indicador_list.html'

class Valor_Indicador_Create(CreateView):
    model = Valor_Indicador
    template_name: str = 'indicadores/valor_indicador/valor_indicador_form.html'
    form_class = Valor_Indicador_Form
    #second_form_class = Indicador_Form
    success_url= reverse_lazy('indicadores:listar_valor_indicador')

    # def get_context_data(self, **kwargs):
    #     context = super(Valor_Indicador_Create, self).get_context_data(**kwargs)
    #     if 'form' not in context:
    #         context['form'] = self.form_class(self.request.GET)
    #     if 'form2' not in context:
    #         context['form2'] = self.second_form_class(self.request.GET)
    #     return context  

    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object
    #     form = self.form_class(request.POST)
    #     form2 = self.second_form_class(request.POST)

    #     if form.is_valid() and form2.is_valid():
    #         solicitud = form.save(commit = False)
    #         solicitud.persona = form2.save() 
    #         solicitud.save()
    #         return HttpResponseRedirect(self.get_success_url())
    #     else :
    #         return self.render_to_response(self.get_context_data(form = form, form2 = form))         


class Valor_Indicador_Update(UpdateView):
    model = Valor_Indicador
    # fields = '__all__'
    form_class = Valor_Indicador_Form
    template_name: str = 'indicadores/valor_indicador/valor_indicador_form.html'
    success_url = reverse_lazy('indicadores:listar_valor_indicador')    


class Valor_Indicador_Delete(DeleteView):
    model = Valor_Indicador
    fields = '__all__'
    template_name: str = 'indicadores/valor_indicador/valor_indicador_delete.html'
    success_url = reverse_lazy('indicadores:listar_valor_indicador')    



class Alarma_Create(CreateView):
    model = Alarma
    form_class = Alarma_Form
    template_name: str = 'indicadores/alarma/alarma_form.html'
    success_url = reverse_lazy('indicadores:listar_alarma')

class Alarma_Delete(DeleteView):
    model = Alarma
    fields = '__all__'
    template_name: str = 'indicadores/alarma/alarma_delete.html'
    success_url = reverse_lazy('indicadores:listar_alarma')    


class Alarma_List(ListView):
    model = Alarma
    template_name: str = 'indicadores/alarma/alarma_list.html'

class Alarma_Update(UpdateView):
    model = Alarma
    # fields = '__all__'
    form_class = Alarma_Form
    template_name: str = 'indicadores/alarma/alarma_form.html'
    success_url = reverse_lazy('indicadores:listar_alarma')    



# vistas basadas en funciones

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