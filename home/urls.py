# home/urls.py
from django.urls import path
from . import views

app_name = 'gerenciar'

urlpatterns = [
    # --- URLs para Categoria ---
    # /gerenciar/categorias/
    path('categorias/', views.CategoriaListView.as_view(), name='lista_categorias'),
    # /gerenciar/categorias/adicionar/
    path('categorias/adicionar/', views.CategoriaCreateView.as_view(), name='adicionar_categoria'),
    # /gerenciar/categorias/editar/1/
    path('categorias/editar/<int:pk>/', views.CategoriaUpdateView.as_view(), name='editar_categoria'),
    # /gerenciar/categorias/deletar/1/
    path('categorias/deletar/<int:pk>/', views.CategoriaDeleteView.as_view(), name='deletar_categoria'),

    # --- URLs para Fornecedor ---
    # /gerenciar/fornecedores/
    path('fornecedores/', views.FornecedorListView.as_view(), name='lista_fornecedores'),
    # /gerenciar/fornecedores/adicionar/
    path('fornecedores/adicionar/', views.FornecedorCreateView.as_view(), name='adicionar_fornecedor'),
    # /gerenciar/fornecedores/editar/1/
    path('fornecedores/editar/<int:pk>/', views.FornecedorUpdateView.as_view(), name='editar_fornecedor'),
    # /gerenciar/fornecedores/deletar/1/
    path('fornecedores/deletar/<int:pk>/', views.FornecedorDeleteView.as_view(), name='deletar_fornecedor'),
]
