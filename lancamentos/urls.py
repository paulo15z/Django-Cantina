from django.urls import path
from . import views

app_name = 'lancamentos'

urlpatterns = [
    # URL para listar todos os lançamentos (Read)
    # Ex: /lancamentos/
    path('', views.LancamentoListView.as_view(), name='lista'),

    # URL para o formulário de adicionar um novo lançamento (Create)
    # Ex: /lancamentos/adicionar/
    path('adicionar/', views.LancamentoCreateView.as_view(), name='adicionar'),

    # URL para o formulário de editar um lançamento existente (Update)
    # Ex: /lancamentos/editar/5/
    path('editar/<int:pk>/', views.LancamentoUpdateView.as_view(), name='editar'),

    # URL para a página de confirmação de exclusão (Delete)
    # Ex: /lancamentos/deletar/5/
    path('deletar/<int:pk>/', views.LancamentoDeleteView.as_view(), name='deletar'),
]
