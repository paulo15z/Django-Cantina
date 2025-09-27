from django.db import models

class Lancamento(models.Model):
    TIPO_CHOICES = [
        ("entrada", "Entrada"),
        ("saida", "Saída"),
    ]
    
    PAGAMENTO_CHOICES = [
        ("dinheiro", "Dinheiro"),
        ("pix", "PIX"),
        ("cartao_credito", "Cartão de Crédito"),
        ("cartao_debito", "Cartão de Débito"),
        ("transferencia_interna", "Transferência Interna"),
        # em breve fiado (caderno)
    ]

    
    descricao = models.CharField(max_length=255)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField(help_text="Data em que a transação ocorreu")
    
    # --- RELAÇÕES COM OUTROS APPS ---
    categoria = models.ForeignKey(
        'home.Categoria', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name="lancamentos"
    )
    fornecedor = models.ForeignKey(
        'home.Fornecedor', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name="lancamentos"
    )
    cartao_credito = models.ForeignKey(
        'cartoes.CartaoCredito', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name="lancamentos"
    )
    # ---------------------------------

    metodo_pagamento = models.CharField(max_length=100, choices=PAGAMENTO_CHOICES)
    observacoes = models.TextField(blank=True, null=True)
    pago = models.BooleanField(default=True, help_text="Indica se a transação afetou o caixa imediatamente")

    class Meta:
        ordering = ['-data', '-id']

    def __str__(self):
        return f"{self.data} - {self.descricao} (R$ {self.valor})"
