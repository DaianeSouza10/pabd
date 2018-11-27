# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Cadastro(models.Model):
	nome=models.CharField(
		max_length=255,
		null=False,
		blank=False)

	matricula=models.CharField('matri',max_length=14)

	




class Reserva (models.Model):
	matri=models.ForeignKey(Reserva, verbose_name='Reserva')

	data=models.DateField(
		null=False,
		blank=False)

	horaentrada=models.TimeField(
		null=False,
		blank=False)

produtos = Reserva.objects.all()
	





	
		