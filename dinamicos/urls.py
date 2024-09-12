from django.urls import path
from .views import index, fichas_prontas, tela_imc, superiores, tela_login

urlpatterns = [
    path('', index, name='index'),
    path('fichas_prontas/', fichas_prontas, name='fichas_prontas'),
    path('tela_imc/', tela_imc, name='tela_imc'),
    path('superiores/', superiores, name='superiores'),
    path('tela_login/', tela_login, name='tela_login'),
]