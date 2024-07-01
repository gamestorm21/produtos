# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produto/<int:produto_id>/', views.detalhe_produto, name='detalhe_produto'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('adicionar_ao_carrinho/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('criar_conta/', views.criar_conta, name='criar_conta'),
    path('login/', views.fazer_login, name='login'),
    path('logout/', views.fazer_logout, name='logout'),
]
