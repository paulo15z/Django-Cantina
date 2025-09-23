from django.urls import path
from . import views

app_name = 'reservas'

urlpatterns = [

    path('', views.ReservaListView.as_view(), name='lista'),

    path('adicionar/', views.ReservaCreateView.as_view(), name='adicionar'),

    path('editar/<int:pk>/', views.ReservaUpdateView.as_view(), name='editar'),

    path('deletar/<int:pk>/', views.ReservaDeleteView.as_view(), name='deletar'),
                   
]