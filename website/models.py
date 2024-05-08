from django.db import models

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
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, blank=False, unique=True)
    email = models.EmailField()
    formacao = models.IntegerField(choices=FORMACAO_CHOICES)

    class Meta:
        verbose_name_plural = "Pesquisadores"