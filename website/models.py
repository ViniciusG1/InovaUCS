from django.db import models

class TipoPesquisador(models.TextChoices):
    ALUNO = 'AL', 'Aluno'
    PROFESSOR = 'PR', 'Professor'

class Pesquisador(models.Model):
    cpf = models.CharField(verbose_name="CPF", max_length=11, blank=False, unique=True)
    nome = models.CharField(max_length=255, blank=False)
    email = models.EmailField()
    tipo = models.CharField(max_length=2, choices=TipoPesquisador.choices)

    class Meta:
        verbose_name_plural = "Pesquisadores"

    def __str__(self):
        return self.nome

class Area(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class SubArea(models.Model):
    nome = models.CharField(max_length=255)
    area = models.ForeignKey(Area, related_name='subareas', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Subáreas"

    def __str__(self):
        return self.nome

class Instituicao(models.Model):
    cnpj = models.CharField(verbose_name="CNPJ", max_length=14, blank=False, unique=True)
    nome = models.CharField(blank=False, max_length=255)
    sigla = models.CharField(blank=False, max_length=12)

    class Meta:
        verbose_name_plural = "Instituições"

    def __str__(self):
        return self.nome

class FormacaoAcademica(models.Model):
    pesquisador = models.ForeignKey(Pesquisador, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    orientador = models.CharField(blank=True, null=True, max_length=255)
    palavras_chave = models.TextField(blank=True, null=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    ano_inicio = models.IntegerField()
    ano_conclusao = models.IntegerField()

    def __str__(self):
        return self.titulo

class Fomento(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome_agencia = models.CharField(blank=True, null=True, max_length=255)
    sigla_agencia = models.CharField(blank=False, max_length=10)
    valor_aportado = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()

    def __str__(self):
        return f"{self.codigo:04} - {self.sigla_agencia}"

class TipoSituacao(models.TextChoices):
    EM_ANDAMENTO = 'EA', 'Em Andamento'
    FINALIZADO = 'FI', 'Finalizado'
    AGUARDANDO_APROVACAO = 'AA', 'Aguardando Aprovação'
    CANCELADO = 'CA', 'Cancelado'
    SUSPENSO = 'SU', 'Suspenso'
    OUTRO = 'OU', 'Outro'

class Projeto(models.Model):
    titulo = models.CharField(blank=False, max_length=255)
    data_inicio = models.DateField()
    data_conclusao = models.DateField(blank=True, null=True)
    fomento = models.ForeignKey(Fomento, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    subareas = models.ManyToManyField(SubArea)
    situacao = models.CharField(max_length=2, choices=TipoSituacao.choices)
    pesquisadores = models.ManyToManyField(Pesquisador)

    def __str__(self):
        return self.titulo

class TipoProducao(models.TextChoices):
    PATENTE = 'PA', 'Patente'
    ARTIGO = 'AR', 'Artigo'
    LIVRO = 'LI', 'Livro'
    RELATORIO = 'RE', 'Relatório'
    OUTRO = 'OU', 'Outro'

class Producao(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    titulo = models.CharField(blank=False, max_length=255)
    tipo_producao = models.CharField(max_length=2, choices=TipoProducao.choices)
    pesquisadores = models.ManyToManyField(Pesquisador)
    data_publicacao = models.DateField()
    descricao = models.TextField()

    def __str__(self):
        return self.titulo
    
