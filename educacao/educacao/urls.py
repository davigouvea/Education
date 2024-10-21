"""
URL configuration for educacao project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path('merenda/', include('merenda.urls')),  # Roteando para o app Merenda
    path('frequencia/', include('frequencia.urls')),  # Roteando para o app Frequência
    path('avaliacao/', include('avaliacao.urls')),  # Roteando para o app Avaliação de Desempenho
    path('transporte/', include('transporte.urls')),  # Transporte escolar
    path('almoxarifado/', include('almoxarifado.urls')),  # Almoxarifado e uniformes
    path('financeiro/', include('gestao_financeira.urls')),  # Gestão financeira
    path('academico/', include('gestao_academica.urls')),  # Gestão acadêmica
    path('api-auth/', include('rest_framework.urls')),  # Autenticação
]

from django.urls import include, path

urlpatterns = [
    path('api/', include('merenda.urls')),  # Adiciona o módulo Merenda
    path('api/', include('almoxarifado.urls')),  # Adiciona o módulo Almoxarifado
    # Continue adicionando os outros módulos...
]
