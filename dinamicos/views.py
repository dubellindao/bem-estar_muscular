from django.shortcuts import render, redirect
from .models import FichaTreino
from .forms import FichaTreinoForm

# Create your views here.

def index (request):
    return render(request, 'dinamicos/index.html')

# CRUD
def fichas_prontas (request):
    ficha = FichaTreino.objects.all()

    context = {
        'ficha': ficha
    }

    return render(request,'dinamicos/fichas_prontas.html', context)


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
    return render(request, 'dinamicos/tela_login.html')