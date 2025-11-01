from django import forms
from .models import Pensionado, Trabajador
from django.forms import ValidationError


BANCOS_CHOICES = [
    ("", "Selecciona un banco"),
    ("BBVA MEXICO", "BBVA México"),
    ("BANAMEX", "Banamex"),
    ("SANTANDER", "Santander"),
    ("HSBC", "HSBC"),
    ("BANORTE", "Banorte"),
    ("INBURSA", "Inbursa"),
    ("SCOTIABANK", "Scotiabank"),
    ("BANCO AZTECA", "Banco Azteca"),
    ("INTERACCIONES", "Interacciones"),
    ("BANSI", "Bansi"),
]

CENTRO_CHOICES = [
    ('', 'Selecciona una opción'),
    ('OFICINA DE TRAFICO DEL PACIFICO', 'Oficina de Tráfico del Pacífico'),
    ('SUBGERENCIA REGIONAL DE GENERACION TERMOELECTRICA OCCIDENTE', 'Subgerencia Regional de Generación Termoeléctrica Occidente'),
    ('CT_GRAL_MANUEL_ALVAREZ_MORENO', 'C.T. Gral. Manuel Álvarez Moreno')
]

class PensionadoForm(forms.ModelForm):
    banco = forms.ChoiceField(
        choices=BANCOS_CHOICES,
        widget=forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-md'})
    )

    class Meta:
        model = Pensionado
        fields = '__all__'
        widgets = {
            'acreedor': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-md'}),
            'nombre': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-md'}),
            'firma_recibo': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-md'}),
            'contrato': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-md'}),
            'escaneado': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-md'}),
            'observaciones': forms.Textarea(attrs={'rows': 3, 'class': 'w-full px-4 py-2 border rounded-md'}),
        }

    def clean_acreedor(self):
        acreedor = self.cleaned_data.get('acreedor')
        if not acreedor:
            raise forms.ValidationError("Este campo es obligatorio.")

        # Si estamos editando y no se cambió el acreedor → no hay error
        if self.instance.pk:
            if Pensionado.objects.filter(acreedor=acreedor).exclude(pk=self.instance.pk).exists():
                return acreedor
        else:
            if Pensionado.objects.filter(acreedor=acreedor).exists():
                raise forms.ValidationError("Ya existe un pensionado con este número de acreedor.")

        return acreedor

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise forms.ValidationError("Este campo es obligatorio.")

        # Si estamos editando y no se cambió el nombre → no hay error
        if self.instance.pk and Pensionado.objects.filter(nombre=nombre, pk=self.instance.pk).exists():
            return nombre

        if Pensionado.objects.filter(nombre=nombre).exists():
            raise forms.ValidationError("Ya existe un pensionado con este nombre.")

        return nombre

    def clean(self):
        cleaned_data = super().clean()

        # Validar campos obligatorios
        required_fields = ['acreedor', 'nombre', 'banco', 'firma_recibo', 'contrato', 'escaneado']
        for field in required_fields:
            if not cleaned_data.get(field):
                self.add_error(field, "Este campo es obligatorio.")

        return cleaned_data

# pensionados/forms.py


BANCOS_CHOICES = [
    ("", "Selecciona un banco"),
    ("BBVA MEXICO", "BBVA México"),
    ("BANAMEX", "Banamex"),
    ("SANTANDER", "Santander"),
    ("HSBC", "HSBC"),
    ("BANORTE", "Banorte"),
    ("INBURSA", "Inbursa"),
    ("SCOTIABANK", "Scotiabank"),
    ("BANCO AZTECA", "Banco Azteca"),
    ("INTERACCIONES", "Interacciones"),
    ("BANSI", "Bansi"),
]

CENTRO_CHOICES = [
    ("", "Selecciona una opción"),
    ("OFICINA DE TRAFICO DEL PACIFICO", "Oficina de Tráfico del Pacífico"),
    ("SUBGERENCIA REGIONAL DE GENERACION TERMOELECTRICA OCCIDENTE", "Subgerencia Regional de Generación Termoeléctrica Occidente"),
    ("CT_GRAL_MANUEL_ALVAREZ_MORENO", "C.T. Gral. Manuel Álvarez Moreno")
]

class TrabajadorForm(forms.ModelForm):
    centro = forms.ChoiceField(
        choices=CENTRO_CHOICES,
        widget=forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-md'})
    )
    banco = forms.ChoiceField(
        choices=BANCOS_CHOICES,
        widget=forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-md'})
    )

    class Meta:
        model = Trabajador
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        required_fields = ['RPE', 'nombre', 'cuenta', 'clabe', 'centro', 'banco', 'tipo_pago',
                           'contrato', 'tipo_contrato', 'carta_datos_bancarios_actualizada']

        for field in required_fields:
            if not cleaned_data.get(field):
                self.add_error(field, "Este campo es obligatorio.")

        return cleaned_data