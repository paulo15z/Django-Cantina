from django import forms
from .models import Lancamento

class LancamentoForm(forms.ModelForm):
    class Meta:
        model = Lancamento
        # Excluímos 'pago' por enquanto, pois ele será controlado pela lógica do sistema
        fields = [
            'descricao', 'tipo', 'valor', 'data', 'categoria', 
            'fornecedor', 'metodo_pagamento', 'cartao_credito', 'observacoes'
        ]
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Lógica para mostrar/esconder o campo de cartão de crédito
        # pode ser adicionada aqui com Javascript no template,
        # ou com validações no método clean().
        self.fields['cartao_credito'].queryset = self.fields['cartao_credito'].queryset.filter(ativo=True)
