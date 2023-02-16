from pyexpat import model
from tkinter import CASCADE
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


    def __str__(self) -> str:
        return self.nombre




class Valor_Indicador(models.Model):
    valor = models.FloatField()
    valor_en_porcentaje = models.CharField(max_length=10)
    fecha = models.DateField()
    indicador = models.ForeignKey(Indicador, null=True,blank=True, on_delete= models.CASCADE) # 1 Indicador-- * valores

class Alarma(models.Model):
    valor_alerta = models.FloatField()       
    nivel_alarma = models.IntegerField()
    estado_alarma = models.BooleanField()
    fecha = models.DateField()

    # 1 Alarma es generada por 1/* valores de indicadores
    valor_de_indicador = models.ForeignKey(Valor_Indicador, null=True,blank=True, on_delete= models.CASCADE) # 1 Indicador-- * valores

class Medida(models.Model):
    medidas_tomadas = models.TextField() 
    fecha_de_la_medida = models.DateField()
    indicador = models.ForeignKey(Indicador, null=True,blank=True, on_delete= models.CASCADE) # 1 Indicador-- * valores
    alarma = models.ForeignKey(Alarma, null=True,blank=True, on_delete= models.CASCADE) # 1 Indicador-- * valores
    

