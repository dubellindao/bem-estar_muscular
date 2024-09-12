from django.shortcuts import render

# Create your views here.

def index (request):
    return render(request, 'dinamicos/index.html')

def fichas_prontas (request):
    return render(request, 'dinamicos/fichas_prontas.html')

def tela_imc (request):
    return render(request, 'dinamicos/tela_imc.html')

def superiores (request):
    return render(request, 'dinamicos/superiores.html')

def tela_login (request):
    return render(request, 'dinamicos/tela_login.html')