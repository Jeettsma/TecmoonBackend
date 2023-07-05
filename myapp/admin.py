from django.contrib import admin

from .models import Marca, producto_notebook,producto_pc, producto_celulare, Contacto, transicione
# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'precio', 'marca']
    search_fields = ['nombre']
    list_per_page = 5
    list_filter = ['marca','precio']
admin.site.register(Marca)    
admin.site.register(producto_notebook,ProductoAdmin)
admin.site.register(producto_pc,ProductoAdmin)
admin.site.register(producto_celulare,ProductoAdmin)
admin.site.register(Contacto)
admin.site.register(transicione)
