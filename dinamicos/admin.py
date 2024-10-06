from django.contrib import admin
from .models import Usuario, FichaTreino, CalculoImc
# Register your models here.

admin.site.register(Usuario)

admin.site.register(FichaTreino)

admin.site.register(CalculoImc)