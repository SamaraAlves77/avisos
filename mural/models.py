from django.db import models


class Categoria(models.Model):
    nome=models.CharField(max_length=50, unique=True)


class Aviso(models.Model):
    titulo=models.CharField(max_length=100)
    conteudo=models.TextField()
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    data_criacao=models.DateTimeField(auto_now_add=True)


