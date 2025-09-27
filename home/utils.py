# home/utils.py (VERSÃO CORRIGIDA)

from lancamentos.models import Lancamento
from django.db.models import Sum
from decimal import Decimal

def calcular_total_entradas(queryset=None):
    """
    Calcula o total de entradas pagas.
    Pode receber um queryset pré-filtrado (ex: por data).
    """
    # Se nenhum queryset for fornecido, usa todos os lançamentos.
    if queryset is None:
        queryset = Lancamento.objects.all()
    
    return queryset.filter(
        tipo='entrada', 
        pago=True
    ).aggregate(total=Sum('valor'))['total'] or Decimal('0.00')

def calcular_total_saidas_caixa(queryset=None):
    """
    Calcula o total de saídas que afetaram o caixa (pagas).
    Exclui despesas de cartão de crédito não pagas.
    Pode receber um queryset pré-filtrado.
    """
    # Se nenhum queryset for fornecido, usa todos os lançamentos.
    if queryset is None:
        queryset = Lancamento.objects.all()
        
    return queryset.filter(
        tipo='saida', 
        pago=True
    ).aggregate(total=Sum('valor'))['total'] or Decimal('0.00')

def calcular_saldo_caixa(queryset=None):
    """
    Calcula o saldo líquido do caixa (entradas pagas - saídas pagas).
    Pode receber um queryset pré-filtrado.
    """
    # --- CORREÇÃO APLICADA AQUI ---
    # Garante que a variável 'queryset' local tenha um valor ANTES de ser usada.
    if queryset is None:
        queryset = Lancamento.objects.all()
    
    # Agora, 'queryset' sempre terá um valor válido para ser passado.
    entradas = calcular_total_entradas(queryset)
    saidas = calcular_total_saidas_caixa(queryset)
    return entradas - saidas
