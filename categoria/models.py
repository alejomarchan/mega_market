from enum import unique
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models.fields import CharField, TextField, SlugField
from django.db.models.fields.files import ImageField
from django.urls import reverse

# Create your models here.
class Categoria(models.Model):
    categoria_nombre = CharField(max_length=50, unique=True)
    slug = SlugField(max_length=100, unique=True)
    descripcion = TextField(max_length=255, blank=True)
    cat_image = ImageField(upload_to="images/categorias", blank=True)

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = 'categorias'

    def get_url(self):
        return reverse('store:producto_por_categoria', args=[self.slug])


    def __str__(self):
        return self.categoria_nombre