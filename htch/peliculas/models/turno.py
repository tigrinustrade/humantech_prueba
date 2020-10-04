"""Models Turno"""
from datetime import date

from django.core.exceptions import ValidationError
from django.db import models

from htch.utils.models import HumantechModel


def fecha_validator(value):
    if value < date.today():
        raise ValidationError('La fecha para el turno es inferior a la actual')

def hora_validator(value):
    if len(value) != 5:
        raise ValidationError('Utilice el formato de hora HH:MM')
    if value.find(":") != 2:
        raise ValidationError('Utilice el formato de hora HH:MM')
    hor = int(value[0:2])
    if hor < 0 or hor >23:
         raise ValidationError('Utilice el formato de hora HH:MM')

class Turno(HumantechModel):
    id_turno = models.AutoField(primary_key=True)
    turno_fech = models.DateField(validators=[fecha_validator])
    turno_hora = models.CharField(validators=[hora_validator], max_length=5)
    turno_estado = models.BooleanField()
    pelicula = models.ForeignKey('peliculas.Pelicula', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "Fecha {}".format(self.turno_fech)

    class Meta(HumantechModel.Meta):
        db_table = 't_turno'
        verbose_name_plural = "Turnos"
        ordering = ['turno_hora']
