from django.shortcuts import render
from store.models import Producto

# Create your views here.
def home(request):
    productos = Producto.objects.all().filter(is_available=True)
    return render(request, 'home.html', {'productos': productos})