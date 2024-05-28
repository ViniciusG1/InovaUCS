from django.db import models
from django.contrib import admin

class Pesquisador(models.Model):

    GRADUACAO = 1
    ESPECIALIZACAO = 2
    MBA = 3
    MESTRADO = 4
    DOUTORADO = 5

    FORMACAO_CHOICES = [
        (GRADUACAO, 'Graduação'),
        (ESPECIALIZACAO, 'Especialização'),
        (MBA, 'MBA'),
        (MESTRADO, 'Mestrado'),
        (DOUTORADO, 'Doutorado'),
    ]

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, blank=False, name='Nome')
    cpf = models.CharField(max_length=11, blank=False, unique=True, name="CPF")
    email = models.EmailField()
    formacao = models.IntegerField(choices=FORMACAO_CHOICES)

    class Meta:
        verbose_name_plural = "Pesquisadores"


class Instituicao(models.Model):

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, blank=False, name="Nome")
    cnpj = models.CharField( max_length=14, blank=False, unique=True, name="CNPJ")

    class Meta:
        verbose_name_plural = "Instituições"


class TipoProducao(models.Model):

    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=20, blank=False)


    class Meta:
        verbose_name_plural = "Tipo de Produções"

    def __str__(self):
        return self.tipo

class Producao(models.Model):

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=20, blank=False, name="Título")
    tipo = models.ForeignKey(TipoProducao, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Produções"

    def __str__(self):
        return self.titulo

class Fomento(models.Model):

    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100, blank=False, name="Descrição")

    class Meta:
        verbose_name_plural = "Fomentos"

    def __str__(self):
        return self.descricao



class Projeto(models.Model):

    CONCLUIDO = 1
    EM_DESENVOLVIMENTO = 2
    PAUSADO = 3
    CANCELADO = 4
    EM_PLANEJAMENTO = 5
    EM_REVISAO = 6
    TESTES = 7

    RESULTADO_CHOICES = [
        (CONCLUIDO, 'Concluído'),
        (EM_DESENVOLVIMENTO, 'Fase de Desenvolvimento'),
        (PAUSADO, 'Pausado'),
        (CANCELADO, 'Cancelado'),
        (EM_PLANEJAMENTO, 'Fase de Planejamento'),
        (EM_REVISAO, 'Fase de Revisão'),
        (TESTES, 'Fase de Testes'),
    ]


    titulo = models.CharField(max_length=100, blank=False)
    dataInicio = models.DateField('Data de Inicio', blank=False)
    dataFinal = models.DateField('Data de Conclusão')
    fomento = models.ForeignKey(Fomento, on_delete=models.CASCADE)
    #Area?
    #SubArea?
    producao = models.ForeignKey(Producao, on_delete=models.CASCADE, name="Produção")
    resultado = models.IntegerField(choices=RESULTADO_CHOICES, null=False)

    class Meta:
        verbose_name_plural = "Projetos"