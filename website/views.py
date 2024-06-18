from django.contrib import admin
from django.shortcuts import render
from website.models import *

class PesquisadorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'email', 'tipo']
    search_fields = ['nome', 'cpf', 'email']
    list_filter = ['tipo']

class AreaAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']

class SubAreaAreaFilter(admin.SimpleListFilter):
    title = 'Área'  # Título exibido no filtro
    parameter_name = 'area'  # Nome do parâmetro no URL

    def lookups(self, request, model_admin):
        # Retorna uma lista de tuplas (chave, valor) para as opções de filtro
        areas = Area.objects.all().order_by('nome')
        return [(area.id, area.nome) for area in areas]

    def queryset(self, request, queryset):
        # Filtra o queryset de SubArea com base no parâmetro de filtro 'area'
        if self.value():
            return queryset.filter(area__id=self.value())

class SubAreaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'area']
    search_fields = ['nome']
    list_filter = [SubAreaAreaFilter]

class SiglaAgenciaFilter(admin.SimpleListFilter):
    title = 'Sigla da Agência de Fomento'
    parameter_name = 'sigla_agencia'

    def lookups(self, request, model_admin):
        # Obter todas as siglas únicas de agências de fomento
        fomentos = model_admin.get_queryset(request).values_list('fomento__sigla_agencia', flat=True).distinct()
        return [(sigla, sigla) for sigla in fomentos if sigla]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(fomento__sigla_agencia=self.value())
        return queryset

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'data_inicio', 'area', 'situacao']
    search_fields = ['titulo', 'pesquisadores__nome']  # Adicionando pesquisadores__nome
    list_filter = ['situacao', SubAreaAreaFilter, SiglaAgenciaFilter]

class ProducaoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'data_publicacao', 'tipo_producao', 'projeto']
    search_fields = ['titulo', 'pesquisadores__nome', 'projeto__titulo'] 
    list_filter = ['tipo_producao'] 

class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sigla', 'cnpj']
    search_fields = ['nome', 'sigla', 'cnpj'] 

class FormacaoAcademicaAdmin(admin.ModelAdmin):
    list_display = ['pesquisador', 'titulo', 'instituicao', 'area', 'ano_inicio', 'ano_conclusao']
    search_fields = ['pesquisador__nome', 'titulo', 'instituicao__nome', 'instituicao__sigla'] 
    list_filter = ['area']

class FomentoAdmin(admin.ModelAdmin):
    list_display = ['sigla_agencia', 'codigo', 'nome_agencia', 'valor_aportado']
    search_fields = ['codigo', 'sigla_agencia', 'nome_agencia', 'valor_aportado'] 
    list_filter = ['sigla_agencia']
