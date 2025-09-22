# reservas/models.py
from django.db import models
from decimal import Decimal

# Renomeamos Cofrinho para Reserva
class Reserva(models.Model):
    nome = models.CharField(max_length=100)
    objetivo = models.TextField(blank=True)
    meta = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nome']
    def __str__(self):
        return self.nome
    # ... (propriedades como saldo_atual virão depois)

# Renomeamos MovimentoCofrinho para MovimentoReserva
class MovimentoReserva(models.Model):
    TIPO_CHOICES = [('deposito', 'Depósito'), ('resgate', 'Resgate')]
    
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name='movimentos')
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)
    
    lancamento_geral = models.OneToOneField(
        'lancamentos.Lancamento', 
        on_delete=models.SET_NULL, 
        null=True, blank=True,
        related_name='movimento_reserva'
    )

    class Meta:
        ordering = ['-data']
    def __str__(self):
        return f"{self.get_tipo_display()} de R$ {self.valor} em {self.reserva.nome}"
