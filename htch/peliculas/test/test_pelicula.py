"""Test de peliculas"""
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from htch.peliculas.models import Pelicula, Turno
from htch.users.models import User


class PeliculasTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.creat(
            first_name='Evaluador',
            last_name='Principal',
            username='EP',
            password='akam1022AK',
            email='evaluadorprincipal@gmail.com',
            is_superuser=True
        )
        self.pelicula = Pelicula.objects.create(
            peli_nom = 'El Silencio de los Inocentes',
            peli_img='http://firebase.com/00018.jpg',
            peli_publi='2020-11-01',
            peli_estado=true
        )
        self.url_peliculas = '/apiPelicula/pelicula/'
    def test_listar_peliculas(self):
        request = self.client.get(self.url_peliculas)
        self.assertEqual(request.status_code, status.HTTP_200_ok)