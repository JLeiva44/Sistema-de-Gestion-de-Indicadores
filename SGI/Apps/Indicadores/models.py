from pyexpat import model
from django.db import models

# Create your models here.

class Indicador(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField()
    estado = models.CharField(max_length=30)
    fecha_estad0 = models.DateField()
    min_valor = models.FloatField()
    med_valor = models.FloatField()
    max_valor = models.FloatField()
    valor_critico = models.FloatField()
    frecuencia = models.IntegerField()
    irregularidades = models.TextField()
    unidad_valor = models.CharField(max_length=10) # Revisar esto
    correos = models.EmailField()

class Medida(models.Model):
    medidas_tomadas = models.TextField() 
    fecha_de_la_medida = models.DateField()


class Valor_Indicador(models.Model):
    valor = models.FloatField()
    valor_en_porcentaje = models.CharField(max_length=10)
    fecha = models.DateField()

class Alarma(models.Model):
    valor_alerta = models.FloatField()       
    nivel_alarma = models.IntegerField()
    estado_alarma = models.BooleanField()
    fecha = models.DateField()

