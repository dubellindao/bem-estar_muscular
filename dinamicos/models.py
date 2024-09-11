from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=30)

    def __str__(self):
        return self.nome
        
class Calculo_imc(models.Model):
    data = models.DateField()
    imc = models.CharField(max_length=50)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

    def __str__(self):
        return self.imc

class Ficha_treino(models.Model):
    data_criacao = models.DateField()
    segunda_feira = models.CharField(max_length=100)
    terca_feira = models.CharField(max_length=100)
    quarta_feira = models.CharField(max_length=100)
    quinta_feira = models.CharField(max_length=100)
    sexta_feira = models.CharField(max_length=100)
    sabado = models.CharField(max_length=100)
    domingo = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

    def __str__ (self):
        return self.data_criacao