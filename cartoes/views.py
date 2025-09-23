from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import CartaoCredito
from .forms import CartaoCreditoForm


class CartaoListView(ListView):
    """View para listar todos os cartões de crédito."""
    model = CartaoCredito
    template_name = 'cartoes/lista.html'
    context_object_name = 'cartoes'
    queryset = CartaoCredito.objects.filter(ativo=True) # nao mostra cartoes inativos

class CartaoCreateView(CreateView):
    """View para adicionar um novo cartão."""
    model = CartaoCredito
    form_class = CartaoCreditoForm
    template_name = 'cartoes/formulario.html'
    success_url = reverse_lazy('cartoes:lista')

class CartaoUpdateView(UpdateView):
    """View para editar um cartão existente."""
    model = CartaoCredito
    form_class = CartaoCreditoForm
    template_name = 'cartoes/formulario.html'
    success_url = reverse_lazy('cartoes:lista')

class CartaoDeleteView(DeleteView):
    """View para deletar um cartão."""
    model = CartaoCredito
    template_name = 'cartoes/confirmar_delete.html'
    success_url = reverse_lazy('cartoes:lista')