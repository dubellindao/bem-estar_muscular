from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=30)

    def __str__(self):
        return self.nome
        
class CalculoImc(models.Model):
    data = models.DateField()
    imc = models.CharField(max_length=50)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

    def __str__(self):
        return self.imc

class FichaTreino(models.Model):
    nome = models.CharField(max_length=100)
    segunda = models.CharField(max_length=100)
    terca = models.CharField(max_length=100)
    quarta = models.CharField(max_length=100)
    quinta = models.CharField(max_length=100)
    sexta = models.CharField(max_length=100)
    sabado = models.CharField(max_length=100)
    domingo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome