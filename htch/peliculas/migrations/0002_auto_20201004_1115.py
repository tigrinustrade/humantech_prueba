# Generated by Django 3.0.10 on 2020-10-04 15:15

from django.db import migrations, models
import htch.peliculas.models.turno


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno',
            name='turno_hora',
            field=models.CharField(max_length=5, validators=[htch.peliculas.models.turno.hora_validator]),
        ),
    ]