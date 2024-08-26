from django.contrib import admin
from .models import Empresa, Slider


class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'documento', 'telefone')
    list_filter = ('created', 'nome')
    

class SliderAdmin(admin.ModelAdmin):
     prepopulated_fields = {"slug": ("titulo",)}
     list_display = ('titulo', 'categoria', 'created')
     list_filter = ('created', 'titulo')    
    

admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Slider, SliderAdmin)

