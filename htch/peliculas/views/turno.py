"""View Turno"""
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from htch.peliculas.models import Turno
from htch.peliculas.serializers import TurnoModelSerializer
from htch.peliculas.permissions.pelicula import IsPeliculaAdminSuper


class TurnoViewSet(viewsets.ModelViewSet):
    queryset = Turno.objects.all()
    serializer_class = TurnoModelSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = [AllowAny]
        else:
            permissions = [IsPeliculaAdminSuper]
        return [p() for p in permissions]
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)