from django import forms
from .models import Pensionado, Trabajador


class PensionadoForm(forms.ModelForm):
    class Meta:
        model = Pensionado
        fields = ['acreedor', 'nombre', 'banco', 'firma_recibo', 'contrato', 'escaneado', 'observaciones']
        widgets = {
            'acreedor': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-cfe-green-600 focus:border-transparent'}),
            'nombre': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-cfe-green-600 focus:border-transparent'}),
            'banco': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-cfe-green-600 focus:border-transparent'}),
            'firma_recibo': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-cfe-green-600 focus:border-transparent'}),
            'contrato': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-cfe-green-600 focus:border-transparent'}),
            'escaneado': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-cfe-green-600 focus:border-transparent'}),
            'observaciones': forms.Textarea(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-cfe-green-600 focus:border-transparent', 'rows': 3}),
        }
        labels = {
            'acreedor': 'Acreedor',
            'nombre': 'Nombre',
            'banco': 'Banco',
            'firma_recibo': 'Firma Recibo',
            'contrato': 'Contrato',
            'escaneado': 'Escaneado',
            'observaciones': 'Observaciones',
        }


class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = ['RPE', 'nombre', 'cuenta', 'clabe', 'centro', 'banco', 'tipo_pago', 'contrato', 'tipo_contrato', 'carta_datos_bancarios_actualizada', 'comentarios']
        widgets = {
            'RPE': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-cfe-green-600 focus:border-transparent'}),
            'nombre': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-cfe-green-600 focus:border-transparent'}),
            'cuenta': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-cfe-green-600 focus:border-transparent'}),
            'clabe': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-cfe-green-600 focus:border-transparent'}),
            'centro': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-cfe-green-600 focus:border-transparent'}),
            'banco': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-cfe-green-600 focus:border-transparent'}),
            'tipo_pago': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-cfe-green-600 focus:border-transparent'}),
            'contrato': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-cfe-green-600 focus:border-transparent'}),
            'tipo_contrato': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-cfe-green-600 focus:border-transparent'}),
            'carta_datos_bancarios_actualizada': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-cfe-green-600 focus:border-transparent'}),
            'comentarios': forms.Textarea(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-cfe-green-600 focus:border-transparent', 'rows': 3}),
        }
        labels = {
            'RPE': 'RPE',
            'nombre': 'Nombre',
            'cuenta': 'Cuenta',
            'clabe': 'CLABE',
            'centro': 'Centro',
            'banco': 'Banco',
            'tipo_pago': 'Tipo de Pago',
            'contrato': 'Contrato',
            'tipo_contrato': 'Tipo de Contrato',
            'carta_datos_bancarios_actualizada': 'Carta Datos Bancarios Actualizada',
            'comentarios': 'Comentarios',
        }
