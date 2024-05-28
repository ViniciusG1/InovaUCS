# Generated by Django 5.0.6 on 2024-05-28 23:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fomento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Descrição', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Fomentos',
            },
        ),
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Nome', models.CharField(max_length=50)),
                ('CNPJ', models.CharField(max_length=14, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Instituições',
            },
        ),
        migrations.CreateModel(
            name='Producao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Título', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Produções',
            },
        ),
        migrations.CreateModel(
            name='TipoProducao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Tipo de Produções',
            },
        ),
        migrations.AlterModelOptions(
            name='pesquisador',
            options={'verbose_name_plural': 'Pesquisadores'},
        ),
        migrations.RenameField(
            model_name='pesquisador',
            old_name='cpf',
            new_name='CPF',
        ),
        migrations.RenameField(
            model_name='pesquisador',
            old_name='nome',
            new_name='Nome',
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('dataInicio', models.DateField(verbose_name='Data de Inicio')),
                ('dataFinal', models.DateField(verbose_name='Data de Conclusão')),
                ('resultado', models.IntegerField(choices=[(1, 'Concluído'), (2, 'Fase de Desenvolvimento'), (3, 'Pausado'), (4, 'Cancelado'), (5, 'Fase de Planejamento'), (6, 'Fase de Revisão'), (7, 'Fase de Testes')])),
                ('Produção', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.producao')),
                ('fomento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.fomento')),
            ],
            options={
                'verbose_name_plural': 'Projetos',
            },
        ),
        migrations.AddField(
            model_name='producao',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.tipoproducao'),
        ),
    ]