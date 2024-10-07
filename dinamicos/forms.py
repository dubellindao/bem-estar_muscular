from django import forms 
from .models import FichaTreino

class FichaTreinoForm(forms.ModelForm):
    class Meta:
        model = FichaTreino
        fields = '__all__' 

        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-600',
                'placeholder': 'Digite o nome do usuário',
            }),
            'segunda': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-600',
                'placeholder': 'Ex: Treino de superiores',
            }),
            'terca': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-600',
                'placeholder': 'Ex: Treino de inferiores',
            }),
            'quarta': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-600',
                'placeholder': 'Ex: Cardio',
            }),
            'quinta': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-600',
                'placeholder': 'Ex: Treino de superiores',
            }),
            'sexta': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-600',
                'placeholder': 'Ex: Cardio e Abs',
            }),
            'sabado': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-600',
                'placeholder': 'Ex: Treino de inferiores',
            }),
            'domingo': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-600',
                'placeholder': 'Ex: Descanso',
            }),
        }