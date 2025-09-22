from django import forms
from .models import CartaoCredito

class CartaoCreditoForm(forms.ModelForm):
    class Meta:
        model = CartaoCredito
        fields = ['nome', 'limite_total', 'dia_vencimento', 'dia_fechamento', 'ativo']
        widgets = {
            'dia_vencimento': forms.NumberInput(attrs={'min': 1, 'max': 31}),
            'dia_fechamento': forms.NumberInput(attrs={'min': 1, 'max': 31}),
        }
