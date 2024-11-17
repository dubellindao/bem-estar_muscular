from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.

def quadriceps (request):
    # Lista de exercícios para o quadríceps (pode ser substituída por dados do banco de dados)
    exercicios = [
        {"nome": "Agachamento Livre", "descricao": "O agachamento livre é um exercício completo para os quadríceps, promovendo força e estabilidade nas pernas.", "url": "agachamento_livre"},
        {"nome": "Leg Press", "descricao": "O leg press é um excelente exercício de isolamento para os quadríceps, permitindo treinar com altas cargas.", "url": "leg_press"},
        {"nome": "Afundo", "descricao": "Exercício que trabalha o quadríceps de forma unilateral, promovendo equilíbrio e força.", "url": "afundo"},
        {"nome": "Extensão de Perna", "descricao": "Um movimento isolado que foca diretamente no quadríceps, ideal para definição muscular.", "url": "extensao_perna"},
    ]

    # Paginação (2 exercícios por página)
    paginator = Paginator(exercicios, 2)  # Mostra 2 exercícios por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'inferiores/quadriceps.html', {'page_obj': page_obj})

