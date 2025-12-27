from django.contrib import admin
from .models import Pensionado, Trabajador


@admin.register(Pensionado)
class PensionadoAdmin(admin.ModelAdmin):
    list_display = ['acreedor', 'nombre', 'banco', 'firma_recibo', 'contrato', 'escaneado']
    search_fields = ['acreedor', 'nombre', 'banco']
    list_filter = ['banco', 'firma_recibo']


@admin.register(Trabajador)
class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ['RPE', 'nombre', 'cuenta', 'clabe', 'centro', 'banco', 'tipo_pago']
    search_fields = ['RPE', 'nombre', 'cuenta', 'clabe']
    list_filter = ['banco', 'tipo_pago', 'centro']
