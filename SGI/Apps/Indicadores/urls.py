from django.contrib import admin
from django.urls import path
from Apps.Indicadores import views
import re

app_name = "indicadores"

urlpatterns = [
    path('', views.indicadores_index,name = 'index'),
    path('indicadorform/',views.indicadores_form, name = 'crear_indicador'),
    path('listarindicador/',views.indicador_list, name = 'listar_indicador'),
    path('actualizarindicador/<id_indicador>/',views.indicator_update, name = 'actualizar_indicador'),
    path('eliminarindicador/<id_indicador>/',views.indicator_delete, name = 'eliminar_indicador'),

 

    path('alarmaform/', views.alarma_form, name = 'crear_alarma'),
    path('medidaform/', views.medida_form, name = 'crear_medida'),
    path('valorindicadorform/', views.valor_indicador_form, name = 'crear_valor_de_indicador'),
    path('base/',views.base, name= 'base'),
]
