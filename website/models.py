from django.db import models


class Area(models.Model):
    id = models.AutoField(primary_key=True)
    nomeArea = models.CharField(max_length=50, blank=False)

    class Meta:
        verbose_name_plural = "Areas"

    def __str__(self):
        return self.nomeArea


class SubArea(models.Model):
    id = models.AutoField(primary_key=True)
    nomeSubArea = models.CharField(max_length=50, blank=False)
    tipo = models.ForeignKey(Area, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Subáreas"

    def __str__(self):
        return self.nomeSubArea


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

    ALUNO = 6
    PROFESSOR = 7

    TIPO_PESQ_CHOICES = [
        (ALUNO, 'Aluno(a)'),
        (PROFESSOR, 'Professor(a)'),

    ]

    id = models.AutoField(primary_key=True)
    nomePesq = models.CharField(max_length=50, blank=False)
    cpf = models.CharField(name="CPF", max_length=11, blank=False, unique=True)
    email = models.EmailField()
    formacao = models.IntegerField(name="Formação", choices=FORMACAO_CHOICES)
    tipoPesquisador = models.IntegerField(name="Tipo de Pesquisador",default = 6, choices=TIPO_PESQ_CHOICES)

    class Meta:
        verbose_name_plural = "Pesquisadores"

    def __str__(self):
        return self.nomePesq


class Instituicao(models.Model):

    id = models.AutoField(primary_key=True)
    cnpj = models.CharField(name="CNPJ", max_length=14, blank=False, unique=True)
    nomeInst = models.CharField(max_length=50, blank=False)

    class Meta:
        verbose_name_plural = "Instituições"

    def __str__(self):
        return self.nomeInst


class TipoProducao(models.Model):

    id = models.AutoField(primary_key=True)
    tipoProd = models.CharField(max_length=20, blank=False)


    class Meta:
        verbose_name_plural = "Tipo de Produções"

    def __str__(self):
        return self.tipoProd


class Producao(models.Model):

    id = models.AutoField(primary_key=True)
    tituloProd = models.CharField(max_length=100, blank=False)
    tipo = models.ForeignKey(TipoProducao, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Produções"

    def __str__(self):
        return self.tituloProd

class Fomento(models.Model):

    id = models.AutoField(primary_key=True)
    descricaoFom = models.TextField(max_length=300, blank=False)

    class Meta:
        verbose_name_plural = "Fomentos"

    def __str__(self):
        return self.descricaoFom

class Projeto(models.Model):

    CONCLUIDO = 1
    EM_DESENVOLVIMENTO = 2
    PAUSADO = 3
    CANCELADO = 4
    EM_PLANEJAMENTO = 5
    EM_REVISAO = 6
    TESTES = 7

    SITUACAO_CHOICES = [
        (CONCLUIDO, 'Concluído'),
        (EM_DESENVOLVIMENTO, 'Fase de Desenvolvimento'),
        (PAUSADO, 'Pausado'),
        (CANCELADO, 'Cancelado'),
        (EM_PLANEJAMENTO, 'Fase de Planejamento'),
        (EM_REVISAO, 'Fase de Revisão'),
        (TESTES, 'Fase de Testes'),
    ]


    tituloProj = models.CharField(max_length=100, blank=False)
    dataInicio = models.DateField('Data de Inicio', blank=False)
    dataFinal = models.DateField('Data de Conclusão')
    fomento = models.ForeignKey(Fomento, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    subarea = models.ForeignKey(SubArea, on_delete=models.CASCADE)
    producao = models.ForeignKey(Producao,name="Produção", on_delete=models.CASCADE)
    resultado = models.TextField(name="Resultado", max_length=300, default= ' ', blank=False)
    situacao = models.IntegerField(choices=SITUACAO_CHOICES, null=False)

    class Meta:
        verbose_name_plural = "Projetos"

    def __str__(self):
        return self.tituloProj
