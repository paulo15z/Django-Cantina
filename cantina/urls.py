"""
URL configuration for cantina project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    #path('lancamentos/', include('lancamentos.urls', namespace='lancamentos')),

    #path('cofrinhos/', include('cofrinhos.urls', namespace='cofrinhos')),

   # path('cartoes/', include('cartoes.urls', namespace='cartoes')),

   # path('relatorios/', include('relatorios.urls', namespace='relatorios')),

  #  path('gerenciar/', include('home.urls', namespace='home_gerencia')),

]
