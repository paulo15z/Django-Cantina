# lancamentos/admin.py
from django.contrib import admin
from .models import Lancamento

@admin.register(Lancamento)
class LancamentoAdmin(admin.ModelAdmin):
    list_display = ('data', 'descricao', 'valor', 'tipo', 'metodo_pagamento', 'pago')
    list_filter = ('pago', 'tipo', 'metodo_pagamento')
