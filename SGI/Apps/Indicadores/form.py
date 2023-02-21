from cProfile import label
from tkinter.tix import Select
from django import forms
from matplotlib import widgets
from Apps.Indicadores.models import Indicador, Alarma, Valor_Indicador, Medida

class Valor_Indicador_Form(forms.ModelForm):

    class Meta :
        model = Valor_Indicador

        fields = [
            'valor',
            'valor_en_porcentaje',
            'fecha',
            'indicador',
        ]

        labels = {
            'valor' : 'Valor',
            'valor_en_porcentaje' : 'Valor en Porcentaje',
            'fecha' : 'Fecha',
            'indicador' : 'Indicador',
        }

        widgets = {
            'valor' : forms.TextInput(attrs={'class' : 'form-control'}),
            'valor_en_porcentaje' : forms.TextInput(attrs={'class' : 'form-control'}),
            'fecha' : forms.DateInput(attrs={'class' : 'forms-control'}),
            'indicador' : forms.Select(attrs = {'class' : 'form-control'}) ,
        }

class Alarma_Form(forms.ModelForm):

    class Meta :
        model = Alarma

        fields = [
            'valor_alerta',
            'nivel_alarma',
            'estado_alarma',
            'fecha',
            'valor_de_indicador',
        ]

        labels = {
            'valor_alerta' : 'Valor de Alerta',
            'nivel_alarma' : 'Nivel de Alarma',
            'estado_alarma' : 'Estado de Alarma',
            'fecha' : 'Fecha',
            'valor_de_indicador' : 'Valor de Indicador',
        }

        widgets = {
            'valor_alerta' : forms.TextInput() ,
            'nivel_alarma' : forms.TextInput() ,
            'estado_alarma' : forms.TextInput() ,
            'fecha' : forms.DateInput(),
            'valor_de_indicador' : forms.Select(),
        }

class Medida_Form(forms.ModelForm):
    
    class Meta:
        model = Medida

        fields = [
            'medidas_tomadas',
            'fecha_de_la_medida',
            'indicador',
            'alarma',
        ]

        labels = {
            'medidas_tomadas' : 'Medidas Tomadas',
            'fecha_de_la_medida' : 'Fecha de la medida',
            'indicador' : 'Indicador',
            'alarma' : 'Alarma',
        }

        widgets = {
            'medidas_tomadas' : forms.TextInput(attrs={'class':'form-control'}),
            'fecha_de_la_medida' : forms.DateInput(attrs={'class': 'form-control'}),
            'indicador' : forms.Select(attrs={'class': 'forms-control'}),
            'alarma' : forms.Select(attrs={'class':'form-control'}),
        }

class Indicador_Form(forms.ModelForm):

    class Meta:
        model = Indicador

        fields = [
            'nombre',
            'tipo',
            'descripcion',
            'estado',
            'fecha_estado',
            'min_valor',
            'med_valor',
            'max_valor',
            'valor_critico',
            'frecuencia',
            'irregularidades',
            'unidad_valor',
            'correos',
        ]
        labels = {
            'nombre' : 'Nombre',
            'tipo' : 'Tipo',
            'descripcion': 'Descripcion',
            'estado' : 'Estado',
            'fecha_estado' : 'Fecha de Estado',
            'min_valor' : 'Valor Minimo' ,
            'med_valor' : 'Valor Medio',
            'max_valor' : 'Valor Medio',
            'valor_critico': 'Valor Critico',
            'frecuencia' : 'Frecuencia',
            'irregularidades' : 'Irregularidades',
            'unidad_valor' : 'Unidad de valor',
            'correos' : 'Correos',

        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
            'tipo' : forms.TextInput(attrs={'class' : 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class' : 'form-control'}),
            'estado' : forms.TextInput(attrs={'class' : 'form-control'}),
            'fecha_estado' : forms.DateInput(attrs={'class' : 'form-control'}),
            'min_valor' : forms.TextInput(attrs={'class' : 'form-control'}) ,
            'med_valor' : forms.TextInput(attrs={'class' : 'form-control'}),
            'max_valor' : forms.TextInput(attrs={'class' : 'form-control'}),
            'valor_critico': forms.TextInput(attrs={'class' : 'form-control'}),
            'frecuencia' : forms.TextInput(attrs={'class' : 'form-control'}),
            'irregularidades' : forms.TextInput(attrs={'class' : 'form-control'}),
            'unidad_valor' : forms.TextInput(attrs={'class' : 'form-control'}),
            'correos' : forms.EmailInput(attrs={'class' : 'form-control'}),

        }
