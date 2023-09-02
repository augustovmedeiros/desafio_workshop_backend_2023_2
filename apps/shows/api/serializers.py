from rest_framework import serializers
from apps.shows.models import Categoria, Artista, Show


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ["id", "nome"]


class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = ["id", "nome"]


class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields = ["id", "nome", "data", "categoria", "artistas"]
