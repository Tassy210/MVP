from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('footer/', views.footer, name='footer'),
    path('extensoes/', views.extensoes, name='extensoes'),
    path('sobre/', views.sobre, name='sobre'),   
    path('contato/', views.contato, name='contato'),
    path('projeto/<int:idAcao>/', views.projeto, name='projeto'),
    path('criarAcao/', views.criarAcao, name='criarAcao'),
    path('cidades/<int:idEstado>/', views.cidades_por_estado, name='cidades_por_estado'),
]