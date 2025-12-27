from django.db import models


class Pensionado(models.Model):
    acreedor = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=200, unique=True)
    banco = models.CharField(max_length=100)
    firma_recibo = models.CharField(max_length=100)
    contrato = models.CharField(max_length=100)
    escaneado = models.CharField(max_length=100)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"{self.acreedor} - {self.nombre}"

    class Meta:
        verbose_name = "Pensionado"
        verbose_name_plural = "Pensionados"


class Trabajador(models.Model):
    RPE = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=200, unique=True)
    cuenta = models.CharField(max_length=100)
    clabe = models.CharField(max_length=18)
    centro = models.CharField(max_length=100)
    banco = models.CharField(max_length=100)
    tipo_pago = models.CharField(max_length=50)
    contrato = models.CharField(max_length=100)
    tipo_contrato = models.CharField(max_length=100)
    carta_datos_bancarios_actualizada = models.CharField(max_length=100)
    comentarios = models.TextField(blank=True)

    def __str__(self):
        return f"{self.RPE} - {self.nombre}"

    class Meta:
        verbose_name = "Trabajador"
        verbose_name_plural = "Trabajadores"
