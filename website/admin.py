from django.contrib import admin
from website.models import *
from website.views import *

admin.site.register(Pesquisador, PesquisadorAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(SubArea, SubAreaAdmin)
admin.site.register(Instituicao, InstituicaoAdmin)
admin.site.register(FormacaoAcademica, FormacaoAcademicaAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Producao, ProducaoAdmin)
admin.site.register(Fomento, FomentoAdmin)