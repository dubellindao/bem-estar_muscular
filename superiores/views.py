from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.

def peito (request):
    exercicios = [
        {"nome": "Flexão de braço", "descricao": "Um excelente exercício agrupatório e que foca contração máxima do músculo peitoral.", "url": "flexao"},
        {"nome": "Supino Reto", "descricao": "O supino reto é um dos exercícios mais conhecidos e eficazes para trabalhar o peitoral maior.", "url": "supino_reto"},
        {"nome": "Crucifixo", "descricao": "Exercício isolador que trabalha a extensão e alongamento do peitoral.", "url": "crucifixo"},
        {"nome": "Supino Inclinado", "descricao": "Foco na parte superior do peitoral para maior definição.", "url": "supino_inclinado"},
        # Adicione mais exercícios se necessário
    ]
    
    # Paginação com 2 exercícios por página
    paginator = Paginator(exercicios, 2)  # Mostra 2 exercícios por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'superiores/peito.html', {'page_obj': page_obj})

def biceps (request):
    return render(request, 'superiores/biceps.html')

def triceps (request):
    return render(request, 'superiores/triceps.html')