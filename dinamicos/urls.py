from django.urls import path
from .views import index, fichas_prontas, tela_imc, superiores, inferiores, tela_login, tela_cadastro, cadastrar_ficha, editar_ficha, remover_ficha
from superiores.views import peito, biceps, triceps
from inferiores.views import quadriceps
from exercicios.views import flexao, rosca_direta, triceps_barra, agachamento_livre

urlpatterns = [
    path('', index, name='index'),
    path('fichas_prontas/', fichas_prontas, name='fichas_prontas'),
    path('cadastrar_ficha/', cadastrar_ficha, name='cadastrar_ficha'),
    path('editar_ficha/<int:id>/', editar_ficha, name='editar_ficha'),
    path('remover_ficha/<int:id>/', remover_ficha, name='remover_ficha'),
    path('tela_imc/', tela_imc, name='tela_imc'),
    path('superiores/', superiores, name='superiores'),
    path('inferiores/', inferiores, name='inferiores'),
    path('tela_login/', tela_login, name='tela_login'),
    path('tela_cadastro/', tela_cadastro, name='tela_cadastro'),

    # Caminhos para os músculos
    path('peito/', peito, name='peito'),
    path('biceps/', biceps, name='biceps'),
    path('triceps/', triceps, name='triceps'),
    path('quadriceps/', quadriceps, name='quadriceps'),


    # Caminhos para os exercícios
    path('flexao/', flexao, name='flexao'),
    path('rosca_direta/', rosca_direta, name='rosca_direta'),
    path('triceps_barra/', triceps_barra, name='triceps_barra'),
    path('agachamento_livre/', agachamento_livre, name='agachamento_livre'),
]