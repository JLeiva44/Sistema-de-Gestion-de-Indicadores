from django.contrib import admin
from django.urls import path
from Apps.Indicadores import views

urlpatterns = [
    path('index/', views.indicadores_index,name = 'index'),
    path('indicadorform/',views.indicadores_form, name = 'crear_indicador'),
    path('base/',views.base, name= 'base'),
]
