from django.contrib import admin
from cadastros.models import TabelaCSS, TabelaIRPF, AliquotaCSS, AliquotaIRPF

class AliquotaCSSInline(admin.TabularInline):
    model = AliquotaCSS
    extra = 1 

class AliquotaIRPFInline(admin.TabularInline):
    model = AliquotaIRPF
    extra = 1 

@admin.register(TabelaCSS)
class TabelaCSSAdmin(admin.ModelAdmin):
    ordering = ['-ano_vigencia']
    list_display = ('id', 'ano_vigencia')
    list_display_links = ('id', 'ano_vigencia')
    inlines = [AliquotaCSSInline]

@admin.register(TabelaIRPF)
class TabelaIRPFAdmin(admin.ModelAdmin):
    ordering = ['-ano_vigencia']
    list_display = ('id', 'ano_vigencia', 'deducao_dependente_mes')
    list_display_links = ('id', 'ano_vigencia')
    inlines = [AliquotaIRPFInline]