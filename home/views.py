# home/views.py
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Categoria, Fornecedor
from .forms import CategoriaForm, FornecedorForm

# --- View da Dashboard (já existe) ---
class HomeView(TemplateView):
    template_name = 'home/dashboard.html'

# --- Views para Categoria ---
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'home/gerenciar/lista_categoria.html'
    context_object_name = 'categorias'

class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'home/gerenciar/formulario_geral.html'
    success_url = reverse_lazy('gerenciar:lista_categorias')
    extra_context = {'titulo': 'Nova Categoria', 'lista_url': 'gerenciar:lista_categorias'}

class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'home/gerenciar/formulario_geral.html'
    success_url = reverse_lazy('gerenciar:lista_categorias')
    extra_context = {'titulo': 'Editar Categoria', 'lista_url': 'gerenciar:lista_categorias'}

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'home/gerenciar/confirmar_delete_geral.html'
    success_url = reverse_lazy('gerenciar:lista_categorias')
    extra_context = {'item_tipo': 'Categoria'}

# --- Views para Fornecedor ---
class FornecedorListView(ListView):
    model = Fornecedor
    template_name = 'home/gerenciar/lista_fornecedor.html'
    context_object_name = 'fornecedores'

class FornecedorCreateView(CreateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'home/gerenciar/formulario_geral.html'
    success_url = reverse_lazy('gerenciar:lista_fornecedores')
    extra_context = {'titulo': 'Novo Fornecedor', 'lista_url': 'gerenciar:lista_fornecedores'}

class FornecedorUpdateView(UpdateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'home/gerenciar/formulario_geral.html'
    success_url = reverse_lazy('gerenciar:lista_fornecedores')
    extra_context = {'titulo': 'Editar Fornecedor', 'lista_url': 'gerenciar:lista_fornecedores'}

class FornecedorDeleteView(DeleteView):
    model = Fornecedor
    template_name = 'home/gerenciar/confirmar_delete_geral.html'
    success_url = reverse_lazy('gerenciar:lista_fornecedores')
    extra_context = {'item_tipo': 'Fornecedor'}
