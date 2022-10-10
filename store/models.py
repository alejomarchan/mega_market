from django.forms import DateTimeField
from categoria.models import Categoria
from django.db import models
from django.db.models import BooleanField, CharField, DateTimeField ,ImageField, IntegerField, ForeignKey, TextField, SlugField


# Create your models here.
class Producto(models.Model):
    product_name = CharField(max_length=200, unique=True)
    slug         = SlugField(max_length=200, unique=True)
    description  = TextField(max_length=500, blank=True)
    price        = IntegerField()
    imagen       = ImageField(upload_to="images/productos", blank=True)
    stock        = IntegerField()
    is_available = BooleanField(default=True)
    #El campo category es la clave foranea. Por eso lo coloco y tengo que importar el modulo categoría y la clase categoría
    category     = ForeignKey(Categoria, on_delete=models.CASCADE)
    create_date  = DateTimeField(auto_now_add=True)
    modified_date  = DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name