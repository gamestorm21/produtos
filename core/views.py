# core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Produto

def index(request):
    produtos = Produto.objects.all()
    return render(request, 'core/index.html', {'produtos': produtos})

def detalhe_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'core/detalhe_produto.html', {'produto': produto})

@login_required
def carrinho(request):
    carrinho = request.session.get('carrinho', [])
    produtos = Produto.objects.filter(id__in=carrinho)
    return render(request, 'core/carrinho.html', {'produtos': produtos})

@login_required
def adicionar_ao_carrinho(request, produto_id):
    carrinho = request.session.get('carrinho', [])
    carrinho.append(produto_id)
    request.session['carrinho'] = carrinho
    return redirect('carrinho')

def criar_conta(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'core/criar_conta.html', {'form': form})

def fazer_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

def fazer_logout(request):
    logout(request)
    return redirect('index')
