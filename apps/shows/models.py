from django.db import models


class Categoria(models.Model):
    nome = models.CharField(("Nome da Categoria"), max_length=36)

    def __str__(self):
        return self.nome


class Artista(models.Model):
    nome = models.CharField(("Nome do Artista"), max_length=64)

    def __str__(self):
        return self.nome


class Show(models.Model):
    nome = models.CharField(("Nome do Show"), max_length=200)
    data = models.DateField(("Data do Show"), auto_now=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    artistas = models.ManyToManyField(Artista)

    def __str__(self):
        return self.nome
