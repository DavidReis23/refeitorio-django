from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agendCard/', views.agendCard, name='agendCard'),
    path('cardapio/', views.cardapio_semanal, name='cardapio_semanal'),
    path('tela/', views.telaCardSemanal, name='telaCardSemanal'),
]