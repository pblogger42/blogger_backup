from __future__ import unicode_literals

# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from blogger.apps.principal.models import *
from django.db import models

class UserProfile(models.Model):
	user = models.OneToOneField(User, primary_key = True)
	institucion = models.ForeignKey(Institucion, null = True, blank = True)
	foto_usuario = models.ImageField(upload_to = 'img/usuarios/', default = 'img/none.jpg')

	def __str__(self):
		return self.user.username