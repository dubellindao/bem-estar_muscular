from django.contrib import admin
from .models import Usuario, Ficha_treino, Calculo_imc
# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    fields =  ['nome']

@admin.register(Ficha_treino)
class Ficha_treinoAdmin(admin.ModelAdmin):
    fields = ['data_criacao']

@admin.register(Calculo_imc)
class Calculo_imcAdmin(admin.ModelAdmin):
    fields = ['imc']