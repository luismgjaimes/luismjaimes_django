from symtable import Class
from django.contrib import admin

# Register your models here.

from .models import Servicio

# register your models here.

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')


admin.site.register(Servicio, ServicioAdmin)