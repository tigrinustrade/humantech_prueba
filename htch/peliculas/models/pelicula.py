"""Models Pelicula"""
from django.db import models

from htch.utils.models import HumantechModel


class Pelicula(HumantechModel):
    """Una pelicula es la unidad base de una cinemateca
    """
    id_peli = models.AutoField(primary_key=True)
    peli_nom = models.CharField('Nombre de la Pelicula', max_length=100, blank=False, null=False, unique=True)
    peli_img = models.URLField('Image', blank=False, null=False, unique=True)
    peli_publi = models.DateField(blank=False, null=False)
    peli_estado = models.BooleanField('Activo', default=False)

    def __str__(self):
        return self.peli_nom

    class Meta(HumantechModel.Meta):
        db_table = 't_pelicula'
        verbose_name_plural = 'Peliculas'
        ordering = ['peli_nom']
