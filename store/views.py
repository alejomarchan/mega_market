from django.shortcuts import render, get_object_or_404
from .models import Producto
from categoria.models import Categoria

# Create your views here.
def store(request, categoria_slug=None):
    categorias = None
    productos = None
    if categoria_slug != None:
        categorias = get_object_or_404(Categoria,slug=categoria_slug)
        productos = Producto.objects.filter(category=categorias, is_available=True)
        productos_cant = productos.count()
    else:
        productos = Producto.objects.all().filter(is_available=True)
        productos_cant = productos.count()
    context = {
        'productos': productos,
        'productos_cant': productos_cant,
    }
    return render(request, 'store/store.html', context)