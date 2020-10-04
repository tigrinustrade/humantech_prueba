"""Serializer Turno"""
from rest_framework import serializers

from htch.peliculas.models import Turno


class TurnoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = (
            'id_turno', 'turno_fech', 'turno_hora',
            'turno_estado', 'pelicula'
        )

