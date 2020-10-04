"""Django models utilities"""
from django.db import models


class HumantechModel(models.Model):
    """Modelo abstracto para proveer fecha de creacion y modificació"""
    created = models.DateTimeField(
        'creado el',
        auto_now_add=True,
        help_text='Fecha en que el dato fue creado',
        null=True
    )
    modified = models.DateTimeField(
        'modificado el',
        auto_now=True,
        help_text='Fecha en la ue fue modificado por ultima vez',
        null=True
    )

    class Meta:
        """Opciones del meta"""
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']
