from django.contrib import admin

from tienda.models import Producto, Venta

# Register your models here.
@admin.register(Producto)
class ProgramacionTransporteAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'description', 'price', 'quantity']

@admin.register(Venta)
class ProgramacionTransporteAdmin(admin.ModelAdmin):
    list_display = ['id','product', 'quantity_sold', 'date_sold']

