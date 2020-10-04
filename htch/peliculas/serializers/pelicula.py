"""Serializers Pelicula"""
from rest_framework import serializers

from htch.peliculas.models.pelicula import Pelicula


class PeliculaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = (
            'id_peli', 'peli_nom', 'peli_img',
            'peli_publi', 'peli_estado',
            'created', 'modified'
        )
