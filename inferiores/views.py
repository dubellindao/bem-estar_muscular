from django.shortcuts import render

# Create your views here.

def quadriceps (request):
    return render(request, 'inferiores/quadriceps.html')

