from django import forms
from .models import Cofrinho
from decimal import Decimal

class CofrinhoForm(forms.ModelForm):
    class Meta:
        model = Cofrinho
        fields = ['nome', 'objetivo', 'meta']

class OperacaoCofrinhoForm(forms.Form):
    """Formulário único para depósitos e resgates."""
    valor = forms.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        min_value=Decimal('0.01'),
        label="Valor da Operação"
    )
    observacao = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}), 
        required=False
    )
