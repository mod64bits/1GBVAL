from django.contrib import admin
from .models import Categoria

class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nome",)}
    list_display = ('nome', 'slug',)
    list_filter = ('nome',)
    
    
admin.site.register(Categoria, CategoriaAdmin)
