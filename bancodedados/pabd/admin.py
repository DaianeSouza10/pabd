# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from pabd.models import Cadastro
from pabd.models import Reserva

# Register your models here.

admin.site.register(Cadastro)

admin.site.register(Reserva)
