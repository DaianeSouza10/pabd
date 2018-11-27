# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from pabd.models import Reserva

# Create your views here.

def home(request):
	return render (request,'pabd/index.html')

def lista(request):
	lista=Reserva.objects.all().order_by('-id')
	return render(request, 'pabd/lista.html', {'lista_posts':lista})