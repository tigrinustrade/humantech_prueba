"""Model User"""
from django.contrib.auth.models import AbstractUser
from django.db import models

from htch.utils.models import HumantechModel


class User(HumantechModel, AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    email = models.EmailField(
        'Dirección Email',
        unique=True,
        error_messages={
            'unique': 'Ya existe un usuario con ese email'
        }
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username
