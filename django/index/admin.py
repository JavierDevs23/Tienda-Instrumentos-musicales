from django.contrib import admin
from .models import Categoria, Producto, Genero, Persona

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Genero)
admin.site.register(Persona)