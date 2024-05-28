from django.contrib import admin

class PesquisadorAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'Nome', 'CPF', 'email', 'formacao' ]
    search_fields = [ 'Nome', 'CPF', 'email' ]
    list_filter = [ 'formacao' ]
