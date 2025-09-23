from django.urls import path
from . import views

app_name = 'cartoes'

urlpatterns = [
    
    path('', views.CartaoListView.as_view(), name='lista'),

    path('adicionar/', views.CartaoCreateView.as_view(), name='adicionar'),

    path('editar/<int:pk>/', views.CartaoUpdateView.as_view(), name='editar'),

    path('deletar/<int:pk>/', views.CartaoDeleteView.as_view(), name='deletar'),

]