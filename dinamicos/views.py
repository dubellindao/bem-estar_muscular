from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login 
from .models import FichaTreino, Usuario
from .forms import FichaTreinoForm

# Create your views here.

def index (request):

  
    if request.user.is_authenticated:
        usuarios=Usuario.objects.get(email=request.user)

        print(usuarios)

        context ={
            'usuarios': usuarios
        }
    else: 
        context={

        }

    return render(request, 'dinamicos/index.html', context=context)
    

# CRUD

def fichas_prontas (request):

    if request.user.is_authenticated:

        ficha = FichaTreino.objects.all()

        context = {
            'ficha': ficha
        }

        return render(request,'dinamicos/fichas_prontas.html', context)
        
    else:
        return redirect('tela_login')


def cadastrar_ficha (request):

    form = FichaTreinoForm()
   
   
    if request.method == 'POST':

        form = FichaTreinoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fichas_prontas')
    
        
    context = {'form': form}

    return render(request, 'dinamicos/cadastro_ficha.html', context)


def editar_ficha (request, id):

    ficha = FichaTreino.objects.get(id=id)

    if request.method == 'POST':
        form = FichaTreinoForm(request.POST, instance=ficha)
        if form.is_valid():
            form.save()
            return redirect('fichas_prontas')
    else:
        form = FichaTreinoForm(instance=ficha)

    context = {'form': form}

    return render(request,'dinamicos/cadastro_ficha.html', context)


def remover_ficha (reauest, id):
    ficha = FichaTreino.objects.get(id=id)
    ficha.delete()

    return redirect('fichas_prontas')
# FIM CRUD


def tela_imc (request):
    return render(request, 'dinamicos/tela_imc.html')


def superiores (request):
    return render(request, 'dinamicos/superiores.html')


def inferiores (request):
    return render(request, 'dinamicos/inferiores.html')


def tela_login (request):
    if request.method=='POST':
        email = request.POST.get('email')
        senha = request.POST.get('password')

        user=authenticate(username=email, password=senha)

        if user:
            login(request, user)
            return redirect('index')
        else:
            print('Dados inválidos')

    return render(request, 'dinamicos/tela_login.html')

def tela_cadastro (request):

    if request.method=='POST':
        nome = request.POST.get("name")
        email = request.POST.get("email")
        senha = request.POST.get("password")

        print(nome, email, senha)

        user = User.objects.filter(username=email)

        if user:
            print("Usuário já existe")
        else:
            usuario = Usuario.objects.create(nome=nome, email=email, senha=senha)
            usuario.save()

            usuario_django = User.objects.create_user(username=email, email=email, password=senha)
            usuario_django.save()
            user_save=authenticate(username=email, password=senha)

            if user_save:
                login(request, user_save)
                print(redirect)

                return redirect('index')
            else:
                print("Dados inválidos")


    return render(request, 'dinamicos/tela_cadastro.html')