from django.contrib import admin
from .models import Indicador, Alarma, Medida, Valor_Indicador
# Register your models here.
admin.site.register(Indicador)
admin.site.register(Alarma)
admin.site.register(Medida)
admin.site.register(Valor_Indicador)
