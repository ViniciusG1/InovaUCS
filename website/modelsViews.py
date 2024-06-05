from django.contrib import admin

class PesquisadorAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'nomePesq', 'cpf', 'email', 'formacao' ]
    search_fields = [ 'nomePesq', 'cpf', 'email' ]
    list_filter = [ 'formacao' ]
