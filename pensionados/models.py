from django.db import models

class Pensionado(models.Model):
    CONTRATO_CHOICES = [
        ('SINDICALIZADO', 'Sindicalizado'),
        ('CONFIANZA', 'Confianza'),
    ]
    FIRMA_RECIBO_CHOICES = [
        ('APLICA', 'Aplica'),
        ('NO_APLICA', 'No Aplica'),
    ]
    ESCANEADO_CHOICES = [
        ('SI', 'Sí'),
        ('NO', 'No'),
    ]

    acreedor = models.CharField(max_length=100, unique=True, verbose_name="Número de Acreedor")
    nombre = models.CharField(max_length=150)
    banco = models.CharField(max_length=100)
    firma_recibo = models.CharField(max_length=20, choices=FIRMA_RECIBO_CHOICES)
    contrato = models.CharField(max_length=20, choices=CONTRATO_CHOICES)
    escaneado = models.CharField(max_length=3, choices=ESCANEADO_CHOICES)
    observaciones = models.TextField(blank=False, null=False)

    def __str__(self):
        return f"{self.acreedor} - {self.nombre}"

    class Meta:
        verbose_name_plural = "Pensionados"
        
        

# models.py

class Trabajador(models.Model):
    RPE = models.CharField(max_length=10, unique=True, verbose_name="R.P.E")
    nombre = models.CharField(max_length=150, unique=True)
    cuenta = models.CharField(max_length=20)
    clabe = models.CharField(max_length=18)
    centro = models.CharField(max_length=255)
    banco = models.CharField(max_length=100)
    tipo_pago = models.CharField(max_length=20, choices=[
        ('INTERBANCARIO', 'Interbancario'),
        ('EFECTIVO', 'Efectivo')
    ])
    contrato = models.CharField(max_length=20, choices=[
        ('ACTIVO', 'Activo'),
        ('JUBILADO', 'Jubilado')
    ])
    tipo_contrato = models.CharField(max_length=20, choices=[
        ('SINDICALIZADO', 'Sindicalizado'),
        ('CONFIANZA', 'Confianza')
    ])
    carta_datos_bancarios_actualizada = models.CharField(max_length=3, choices=[
        ('SI', 'Sí'),
        ('NO', 'No')
    ])
    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.RPE} - {self.nombre}"