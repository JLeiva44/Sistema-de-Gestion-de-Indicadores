from cProfile import label
from django import forms
from matplotlib import widgets
from Apps.Indicadores.models import Indicador

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
            'estado' : forms.CheckboxSelectMultiple(),
            'fecha_estado' : forms.TextInput(attrs={'class' : 'form-control'}),
            'min_valor' : forms.TextInput(attrs={'class' : 'form-control'}) ,
            'med_valor' : forms.TextInput(attrs={'class' : 'form-control'}),
            'max_valor' : forms.TextInput(attrs={'class' : 'form-control'}),
            'valor_critico': forms.TextInput(attrs={'class' : 'form-control'}),
            'frecuencia' : forms.TextInput(attrs={'class' : 'form-control'}),
            'irregularidades' : forms.TextInput(attrs={'class' : 'form-control'}),
            'unidad_valor' : forms.TextInput(attrs={'class' : 'form-control'}),
            'correos' : forms.EmailInput(attrs={'class' : 'form-control'}),

        }
