from django.contrib import admin
from .models import Autor, Artigo


# Register your models here.
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "publicado_em", "eh_destaque")
    shearch_fields = ("titulo", "conteudo")
    list_filter = ("autor__nome", "eh_destaque")
    date_hierarchy = "publicado_em"
    

admin.site.register(Autor)
admin.site.register(Artigo, ArtigoAdmin)



#Em admin.py, crie uma classe ArtigoAdmin(admin.ModelAdmin) e adicione list_display = ('titulo', 'autor', 'publicado_em', 'eh_destaque'). Mude o registro para admin.site.register(Artigo, ArtigoAdmin).