from django.shortcuts import render

# Create your views here.

def flexao (request):
    return render(request, 'exercicios/flexao.html')

def rosca_direta (request):
    return render(request, 'exercicios/rosca_direta.html')

def triceps_barra (request):
    return render(request, 'exercicios/triceps_barra.html')

def agachamento_livre (request):
    return render(request, 'exercicios/agachamento_livre.html')