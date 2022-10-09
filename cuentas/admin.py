from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

#Creación de elemento para mostrar ciertos elementos de la cuenta en el panel
class AccountAdmin(UserAdmin):
    #Acá los elementos que se van a ver en el panel de la cuenta
    list_display = ['email', 'first_name', 'last_name', 'username', 'date_joined', 'last_login','is_active']

    #Estos son los elementos que quiero que tengan la posibilidad de tener hipervinculos
    list_display_links = ('email', 'first_name', 'last_name')

    #Estos elementos solamente podrán ser visualizados pero no modificados
    readonly_fields = ('last_login', 'date_joined')

    #Con esto indico que me ordene el listado de cuentas
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


# Register your models here.
admin.site.register(Account,AccountAdmin)
