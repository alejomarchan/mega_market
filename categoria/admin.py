from django.contrib import admin
from .models import Categoria

#Creando la clase model Admin
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('categoria_nombre',)}
    list_display = ('categoria_nombre','slug')


# Register your models here.
admin.site.register(Categoria,CategoryAdmin)