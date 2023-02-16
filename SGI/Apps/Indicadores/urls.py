from django.contrib import admin
from django.urls import path
from Apps.Indicadores import views

urlpatterns = [
    path('index/', views.indicadores_index,name = 'index'),
    path('base/',views.base, name= 'base'),
]
