from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('footer/', views.footer, name='footer'),
    path('extensoes/', views.extensoes, name='extensoes'),
    path('sobre/', views.sobre, name='sobre'),   
    path('contato/', views.contato, name='contato'),
    path('projeto/', views.projeto, name='projeto'),
]
