from django.urls import path
from .views import index, fichas_prontas, tela_imc, superiores, tela_login, cadastrar_ficha, editar_ficha, remover_ficha

urlpatterns = [
    path('', index, name='index'),
    path('fichas_prontas/', fichas_prontas, name='fichas_prontas'),
    path('cadastrar_ficha/', cadastrar_ficha, name='cadastrar_ficha'),
    path('editar_ficha/<int:id>/', editar_ficha, name='editar_ficha'),
    path('remover_ficha/<int:id>/', remover_ficha, name='remover_ficha'),
    path('tela_imc/', tela_imc, name='tela_imc'),
    path('superiores/', superiores, name='superiores'),
    path('tela_login/', tela_login, name='tela_login'),
]