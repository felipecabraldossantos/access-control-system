from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
import re
from .models import Perfil, Produto

def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)
def cadastro_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')

        Produto.objects.create(
            nome=nome,
            descricao=descricao,
            preco=preco
        )

        return redirect('produto')

    return render(request, 'cadastro_produto.html')

def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

def cadastro_user(request):
    if request.method == 'POST':
        nome_completo = request.POST.get('nome_completo')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request, 'cadastro_user.html', {
                'erro': 'As senhas não conferem.'
            })

        if len(password) < 8:
            return render(request, 'cadastro_user.html', {'erro': 'Mínimo 8 caracteres.'})

        if not re.search(r'[A-Z]', password):
            return render(request, 'cadastro_user.html', {'erro': 'Precisa de letra maiúscula.'})

        if not re.search(r'[a-z]', password):
            return render(request, 'cadastro_user.html', {'erro': 'Precisa de letra minúscula.'})

        if not re.search(r'\d', password):
            return render(request, 'cadastro_user.html', {'erro': 'Precisa de número.'})

        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            return render(request, 'cadastro_user.html', {'erro': 'Precisa de caractere especial.'})

        if not validar_cpf(cpf):
            return render(request, 'cadastro_user.html', {
                'erro': 'CPF inválido.'
            })

        if User.objects.filter(username=email).exists():
            return render(request, 'cadastro_user.html', {
                'erro': 'Usuário já existe.'
            })

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )

        Perfil.objects.create(
            user=user,
            nome_completo=nome_completo,
            cpf=cpf
        )

        return redirect('login')

    return render(request, 'cadastro_user.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=email)
            username = user_obj.username
        except User.DoesNotExist:
            return render(request, 'login.html', {
                'erro': 'Email ou senha inválidos'
            })

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('produto')
        else:
            return render(request, 'login.html', {
                'erro': 'Email ou senha inválidos'
            })

    return render(request, 'login.html')

def index(request):
    return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('login')

def produto(request):
    produtos = Produto.objects.all()
    return render(request, 'produto.html', {'produtos': produtos})
