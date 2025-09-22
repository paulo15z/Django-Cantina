from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Lancamento
from .forms import LancamentoForm

class LancamentoListView(ListView):
    """View para listar todos os lançamentos."""
    model = Lancamento
    template_name = 'lancamentos/lista.html'  
    context_object_name = 'lancamentos'
    ordering = ['-data'] 

class LancamentoCreateView(CreateView):
    """View para adicionar um novo lançamento."""
    model = Lancamento
    form_class = LancamentoForm
    template_name = 'lancamentos/formulario.html'
    success_url = reverse_lazy('lancamentos:lista')

class LancamentoUpdateView(UpdateView):
    """View para editar um lançamento existente."""
    model = Lancamento
    form_class = LancamentoForm
    template_name = 'lancamentos/formulario.html'
    success_url = reverse_lazy('lancamentos:lista')

class LancamentoDeleteView(DeleteView):
    """View para deletar um lançamento."""
    model = Lancamento
    template_name = 'lancamentos/confirmar_delete.html'
    success_url = reverse_lazy('lancamentos:lista')
