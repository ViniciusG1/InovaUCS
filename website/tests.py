from django.test import TestCase
from datetime import date
from .models import *

class ProducaoAssociadaProjetoTestCase(TestCase):
    def setUp(self):
        # Criando pesquisadores
        self.pesquisador1 = Pesquisador.objects.create(
            cpf='12345678912',
            nome='Overlord Test',
            email='test@ucs.br',
            tipo='PR'
        )
        self.pesquisador2 = Pesquisador.objects.create(
            cpf='98765432198',
            nome='Bell Cranel',
            email='bell@ucs.br',
            tipo='AL'
        )

        # Criando fomento
        self.fomento = Fomento.objects.create(
            sigla_agencia='CNPq',
            valor_aportado=5600.00,
            descricao='Fomento para pesquisa científica'
        )

        # Criando área e subárea
        self.area = Area.objects.create(nome='Ciências Naturais')
        self.subarea = SubArea.objects.create(nome='Biologia', area=self.area)

        # Criando projeto associado aos pesquisadores, área, subárea e fomento
        self.projeto = Projeto.objects.create(
            titulo='Projeto de Exemplo',
            data_inicio=date(2023, 1, 1),
            fomento=self.fomento,
            area=self.area,
            situacao='EA'
        )
        self.projeto.subareas.add(self.subarea)
        self.projeto.pesquisadores.add(self.pesquisador1, self.pesquisador2)

        # Criando produção associada ao projeto
        self.producao = Producao.objects.create(
            projeto=self.projeto,
            titulo='Produção de Exemplo',
            tipo_producao='AR',  # Assumindo 'AR' para 'Artigo' conforme TipoProducao
            data_publicacao=date(2024, 1, 1),
            descricao='Artigo de exemplo'
        )

    def test_producoes_associadas_projeto(self):
        producoes = self.projeto.producao_set.all()
        self.assertGreater(len(producoes), 0)
        for producao in producoes:
            self.assertEqual(producao.projeto, self.projeto)

class ProducaoTemPesquisadorTestCase(TestCase):
    def setUp(self):
        self.area = Area.objects.create(nome='Ciências da Computação')
        self.subarea = SubArea.objects.create(nome='Teoria da Computação', area=self.area)
        self.fomento = Fomento.objects.create(
            sigla_agencia='CNPq',
            valor_aportado=100000.00,
            descricao='Fomento para pesquisa científica'
        )
        self.projeto = Projeto.objects.create(
            titulo='Projeto de Exemplo',
            data_inicio=date(2023, 1, 1),
            fomento=self.fomento,
            area=self.area,
            situacao='EA'
        )
        self.projeto.subareas.add(self.subarea)

        self.pesquisador = Pesquisador.objects.create(
            cpf='12345678901',
            nome='Fulano de Tal',
            email='fulano@example.com',
            tipo='AL'
        )
        self.producao = Producao.objects.create(
            projeto=self.projeto,
            titulo='Produção de Exemplo',
            tipo_producao='AR',  # Assumindo 'AR' para 'Artigo' conforme TipoProducao
            data_publicacao=date(2024, 1, 1),
            descricao='Artigo de exemplo'
        )
        self.producao.pesquisadores.add(self.pesquisador)

    def test_pesquisadores_associados_producao(self):
        pesquisadores = self.producao.pesquisadores.all()
        self.assertGreater(len(pesquisadores), 0)
        self.assertTrue(all(p in pesquisadores for p in self.producao.pesquisadores.all()))

class ProjetoTemFomentoTestCase(TestCase):
    def setUp(self):
        self.area = Area.objects.create(nome='Ciências Naturais')
        self.subarea = SubArea.objects.create(nome='Biologia', area=self.area)
        self.fomento = Fomento.objects.create(
            sigla_agencia='CNPq',
            valor_aportado=100000.00,
            descricao='Fomento para pesquisa científica'
        )
        self.projeto = Projeto.objects.create(
            titulo='Projeto de Exemplo',
            data_inicio=date(2023, 1, 1),
            fomento=self.fomento,
            area=self.area,
            situacao='EA'
        )
        self.projeto.subareas.add(self.subarea)

    def test_projeto_tem_fomento(self):
        projeto_com_fomento = Projeto.objects.get(pk=self.projeto.pk)
        self.assertIsNotNone(projeto_com_fomento.fomento)

class ProjetoTemAreaSubareasTestCase(TestCase):
    def setUp(self):
        self.area = Area.objects.create(nome='Ciências Naturais')
        self.subarea = SubArea.objects.create(nome='Biologia', area=self.area)
        self.fomento = Fomento.objects.create(
            sigla_agencia='CNPq',
            valor_aportado=100000.00,
            descricao='Fomento para pesquisa científica'
        )
        self.projeto = Projeto.objects.create(
            titulo='Projeto de Exemplo',
            data_inicio=date(2023, 1, 1),
            fomento=self.fomento,
            area=self.area,
            situacao='EA'
        )
        self.projeto.subareas.add(self.subarea)

    def test_projeto_tem_area_subareas(self):
        projeto_com_area_subareas = Projeto.objects.get(pk=self.projeto.pk)
        self.assertIsNotNone(projeto_com_area_subareas.area)
        self.assertGreater(len(projeto_com_area_subareas.subareas.all()), 0)
        self.assertTrue(all(sa in projeto_com_area_subareas.subareas.all() for sa in self.projeto.subareas.all()))


# Verificar aquivos existentes no banco de dados

from django.core.management import call_command

file_path = 'website/fixtures/dados_website_utf8.json'

class ProducaoExistenteAssociadaProjetoTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command('loaddata', file_path)

    def test_producoes_associadas_projeto_existente(self):
        # Seleciona um projeto existente do banco de dados
        projeto = Projeto.objects.first()
        self.assertIsNotNone(projeto, "Nenhum projeto existente no banco de dados.")
        
        producoes = projeto.producao_set.all()
        self.assertGreater(len(producoes), 0, "Nenhuma produção associada ao projeto existente.")
        
        for producao in producoes:
            self.assertEqual(producao.projeto, projeto)

class ProducaoExistenteTemPesquisadorTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command('loaddata', file_path)

    def test_pesquisadores_associados_producao_existente(self):
        # Seleciona uma produção existente do banco de dados
        producao = Producao.objects.first()
        self.assertIsNotNone(producao, "Nenhuma produção existente no banco de dados.")
        
        pesquisadores = producao.pesquisadores.all()
        self.assertGreater(len(pesquisadores), 0, "Nenhum pesquisador associado à produção existente.")
        
        self.assertTrue(all(p in pesquisadores for p in producao.pesquisadores.all()))

class ProjetoExistenteTemFomentoTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command('loaddata', file_path)

    def test_projeto_tem_fomento_existente(self):
        # Seleciona um projeto existente do banco de dados
        projeto = Projeto.objects.first()
        self.assertIsNotNone(projeto, "Nenhum projeto existente no banco de dados.")
        
        self.assertIsNotNone(projeto.fomento, "Projeto existente não possui fomento associado.")

class ProjetoExistenteTemAreaSubareasTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command('loaddata', file_path)

    def test_projeto_tem_area_subareas_existente(self):
        # Seleciona um projeto existente do banco de dados
        projeto = Projeto.objects.first()
        self.assertIsNotNone(projeto, "Nenhum projeto existente no banco de dados.")
        
        self.assertIsNotNone(projeto.area, "Projeto existente não possui área associada.")
        
        subareas = projeto.subareas.all()
        self.assertGreater(len(subareas), 0, "Projeto existente não possui subáreas associadas.")
        
        self.assertTrue(all(sa in subareas for sa in projeto.subareas.all()))
