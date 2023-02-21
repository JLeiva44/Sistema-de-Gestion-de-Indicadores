from django.contrib import admin
from django.urls import path
from Apps.Indicadores import views
import re

app_name = "indicadores"

urlpatterns = [
    path('', views.indicadores_index,name = 'index'),
    path('indicadorform/',views.Indicador_Create.as_view(), name = 'crear_indicador'),
    path('listarindicador/',views.Indicador_List.as_view(), name = 'listar_indicador'),
    path('actualizarindicador/<pk>/',views.Indicador_Update.as_view(), name = 'actualizar_indicador'),
    path('eliminarindicador/<pk>/',views.Indicador_Delete.as_view(), name = 'eliminar_indicador'),

 

    path('alarmaform/', views.alarma_form, name = 'crear_alarma'),
    path('medidaform/', views.medida_form, name = 'crear_medida'),
    path('valorindicadorform/', views.valor_indicador_form, name = 'crear_valor_de_indicador'),
    path('base/',views.base, name= 'base'),
]
