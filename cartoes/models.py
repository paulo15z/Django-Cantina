from django.db import models
from django.core.exceptions import ValidationError
from decimal import Decimal

class CartaoCredito(models.Model):
    nome = models.CharField(max_length=100, help_text="Ex: Nubank, Itaú, etc.")
    limite_total = models.DecimalField(max_digits=10, decimal_places=2)
    dia_vencimento = models.PositiveSmallIntegerField(help_text="Dia do vencimento da fatura (1-31)")
    dia_fechamento = models.PositiveSmallIntegerField(help_text="Melhor dia para compra (1-31)")
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Cartão de Crédito"
        verbose_name_plural = "Cartões de Crédito"
        ordering = ['nome']

    def __str__(self):
        return self.nome
    
    def limite_disponivel(self):
        """Calcula o limite disponível com base nos lançamentos da fatura aberta."""
        gastos_fatura_aberta = self.lancamentos.filter(
            pago=False # Assumindo um campo 'pago' no Lancamento
        ).aggregate(
            total=models.Sum('valor')
        )['total'] or Decimal('0.00')
        
        return self.limite_total - gastos_fatura_aberta
