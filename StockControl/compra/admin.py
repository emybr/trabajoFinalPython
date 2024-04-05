from django.contrib import admin
from .models import Proveedor, Producto


# Register your models here.

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'dni')
    search_fields = ('nombre', 'apellido')

admin.site.register(Proveedor, ProveedorAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'proveedor')
    search_fields = ('nombre', 'proveedor')



admin.site.register(Producto, ProductoAdmin)