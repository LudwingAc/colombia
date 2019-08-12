import datetime

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse

# Create your models here.

ACTIVE_CHOICES = [
    ('Activo', 'Activo'),
    ('Inactivo', 'Inactivo'),
]


class Municipio(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=250)
    is_active = models.CharField(max_length=10, choices=ACTIVE_CHOICES)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('municipio_edit', kwargs={'pk': self.pk})


class Region(models.Model):
    name = models.CharField(max_length=250)
    code = models.IntegerField(unique=True)
    municipios = models.ManyToManyField(Municipio, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('region_edit', kwargs={'pk': self.pk})