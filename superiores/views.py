from django.shortcuts import render

# Create your views here.

def peito (request):
    return render(request, 'superiores/peito.html')

def biceps (request):
    return render(request, 'superiores/biceps.html')

def triceps (request):
    return render(request, 'superiores/triceps.html')