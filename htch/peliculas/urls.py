"""URLS Pelicula"""
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views.pelicula import PeliculaViewSet
from .views.turno import TurnoViewSet

router = DefaultRouter()
router.register(r'pelicula', PeliculaViewSet, basename='peliculas')
router.register(r'turno', TurnoViewSet, basename='turnos')
urlpatterns = [
    path('', include(router.urls))
]
