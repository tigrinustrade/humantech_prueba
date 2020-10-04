"""View Pelicula"""
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from htch.peliculas.models import Pelicula
from htch.peliculas.serializers import PeliculaModelSerializer
from htch.peliculas.permissions.pelicula import IsPeliculaAdminSuper

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaModelSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = [AllowAny]
        else:
            permissions = [IsPeliculaAdminSuper]
        return [p() for p in permissions]