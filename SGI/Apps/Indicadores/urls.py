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

    path('listarvalor/',views.Valor_Indicador_List.as_view(), name = 'listar_valor_indicador'),
    path('crearvalor/',views.Valor_Indicador_Create.as_view(), name = 'crear_valor_indicador'),
    path('actualizarvalor/<pk>',views.Valor_Indicador_Update.as_view(), name = 'actualizar_valor_indicador'),
    path('eliminarvalor/<pk>',views.Valor_Indicador_Delete.as_view(), name = 'eliminar_valor_indicador'),
    

    path('listaralarma/',views.Alarma_List.as_view(), name = 'listar_alarma'),
    path('crearalarma/',views.Alarma_Create.as_view(), name = 'crear_alarma'),
    path('eliminaralarma/<pk>',views.Alarma_Delete.as_view(), name = 'eliminar_alarma'),
    path('actualizaralarma/<pk>',views.Alarma_Update.as_view(), name = 'actualizar_alarma'),

 

    # path('alarmaform/', views.alarma_form, name = 'crear_alarma'),
    # path('medidaform/', views.medida_form, name = 'crear_medida'),
    # path('valorindicadorform/', views.valor_indicador_form, name = 'crear_valor_de_indicador'),
    path('base/',views.base, name= 'base'),
]
