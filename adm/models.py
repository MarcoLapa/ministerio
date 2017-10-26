# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Publicadores(models.Model):
	PRIV_CONGREGACAO_CHOICES = (
								   ('anciao_cc', 'Ancião - coordenador'),
								   ('anciao_se', 'Ancião - secretário'),
								   ('anciao_ss', 'Ancião - superintendente de serviço'),
								   ('anciao', 'Ancião'),
								   ('servo', 'Servo ministerial'),
								)
	PRIV_MINISTERIO_CHOICES = (
								('PB', 'Publicador'),
								('PR', 'Pioneiro Regular'),
							)
	nome = models.CharField(max_length=100, blank=True, null=True)
	rg = models.CharField(max_length=11, blank=True, null=True)
	dt_nasc = models.CharField(max_length=10, blank=True, null=True)
	dt_batismo = models.CharField(max_length=10, blank=True, null=True)
	email = models.CharField(max_length=32, blank=True, null=True)
	endereco = models.ForeignKey('Enderecos')
	congregacao = models.ForeignKey('Congregacao')
	grupo = models.ForeignKey('Grupos')
	priv_congregacao = models.CharField(max_length=10, choices=PRIV_CONGREGACAO_CHOICES)
	priv_ministerio = models.CharField(max_length=2, choices=PRIV_MINISTERIO_CHOICES)
	

class Congregacao(models.Model):
	numero = models.IntegerField()
	nome  = models.CharField(max_length=100, blank=True, null=True)   
	endereco = models.ForeignKey('Enderecos')
	reuniao_meio = models.CharField(max_length=30, blank=True, null=True) 
	reuniao_fim = models.CharField(max_length=30, blank=True, null=True) 


class Enderecos(models.Model):
	FEDERACAO_CHOICES = (
		('RS', 'Rio Grande do Sul'),
		('SC', 'Santa Catarina'),
		('SP', 'São Paulo')
	)
	logradouro = models.CharField(max_length=100, blank=True, null=True)   
	complemento = models.CharField(max_length=20, blank=True, null=True) 
	numero = models.CharField(max_length=10, blank=True, null=True) 
	bairro = models.CharField(max_length=50, blank=True, null=True) 
	cep = models.CharField(max_length=15, blank=True, null=True) 
	cidade = models.CharField(max_length=50, blank=True, null=True, default='Viamão') 
	estado = models.CharField(max_length=2, choices=FEDERACAO_CHOICES, default='RS')
	pais = models.CharField(max_length=20, blank=True, null=True, default='Brasil') 

class Grupos(models.Model):
	nome  = models.CharField(max_length=100, blank=True, null=True)   
	endereco = models.ForeignKey('Enderecos')
	responsavel = models.CharField(max_length=100, blank=True, null=True)

class Atividades(models.Model):
	PIONEIROAUXILIAR_CHOICES = (
		('', ''),
		('30', 'Pioneiro Auxiliar 30H'),
		('50', 'Pioneiro Auxiliar 50h')
	)
	id_pub = models.ForeignKey('Publicadores')
	anomes = models.CharField(max_length=6, blank=True, null=True)
	qt_publicacoes = models.IntegerField()
	qt_videos = models.IntegerField()
	qt_horas = models.IntegerField()
	qt_revisitas = models.IntegerField()
	qt_estudos = models.IntegerField()
	priv_mes = models.CharField(max_length=2, choices=PIONEIROAUXILIAR_CHOICES, default='')

