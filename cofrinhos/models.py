from django.db import models
from decimal import Decimal

class Cofrinho(models.Model):
    nome = models.CharField(max_length=100)
    objetivo = models.TextField(blank=True)
    meta = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

    @property
    def saldo_atual(self):
        """Calcula o saldo dinamicamente a partir dos movimentos."""
        depositos = self.movimentos.filter(tipo='deposito').aggregate(total=models.Sum('valor'))['total'] or Decimal('0.00')
        resgates = self.movimentos.filter(tipo='resgate').aggregate(total=models.Sum('valor'))['total'] or Decimal('0.00')
        return depositos - resgates

class MovimentoCofrinho(models.Model):
    TIPO_CHOICES = [
        ('deposito', 'Depósito'),
        ('resgate', 'Resgate'),
    ]

    cofrinho = models.ForeignKey(Cofrinho, on_delete=models.CASCADE, related_name='movimentos')
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)
    
    # Relação com o lançamento no caixa principal
    lancamento_geral = models.OneToOneField(
        'lancamentos.Lancamento', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='movimento_cofrinho'
    )

    class Meta:
        ordering = ['-data']

    def __str__(self):
        return f"{self.get_tipo_display()} de R$ {self.valor} em {self.cofrinho.nome}"
