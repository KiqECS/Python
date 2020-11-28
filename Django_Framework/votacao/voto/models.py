from django.db import models

# Create your models here.

class Pergunta(models.Model):
    pergunta_texto = models.CharField(max_length=100)
    data_pub = models.DateTimeField('date published')

class Escolha(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    escolha_texto = models.CharField(max_length=100)
    votos = models.IntegerField(default=0)