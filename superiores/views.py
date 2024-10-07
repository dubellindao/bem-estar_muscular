from django.shortcuts import render

# Create your views here.

def peito (request):
    return render(request, 'superiores/peito.html')

def flexao (request):
    return render(request, 'superiores/flexao.html')