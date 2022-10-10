from django.contrib import admin
from .models import Producto

#Creando la clase model Admin para la visualización en el panel de administración
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('product_name','price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}

# Register your models here.
admin.site.register(Producto,ProductoAdmin)
