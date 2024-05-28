from django.contrib import admin
from website.models import *
from website.modelsViews import *

admin.site.register(Pesquisador, PesquisadorAdmin)
admin.site.register(Instituicao)
admin.site.register(TipoProducao)
admin.site.register(Producao)
admin.site.register(Fomento)
admin.site.register(Projeto)
