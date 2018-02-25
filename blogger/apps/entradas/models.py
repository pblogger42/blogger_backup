from __future__ import unicode_literals

# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from blogger.apps.principal.models import *
from django.utils.text import slugify
from django.db import models

def image_directory_path(instance, filename):
	return 'img/instituciones/{0}/entradas/{1}'.format(instance.institucion.slug_institucion, filename)

class Entrada(models.Model):
	institucion = models.ForeignKey(Institucion)
	usuario = models.ForeignKey(User)
	titulo_entrada = models.CharField(max_length = 50)
	fecha_entrada = models.DateField(auto_now = True)
	fecha_actualizacion_entrada = models.DateField(blank = True, null = True)
	slug_entrada = models.SlugField(max_length = 80, unique = True, blank = True, null = True)
	descripcion_entrada = models.CharField(max_length = 2000)
	imagen_portada = models.ImageField(upload_to = image_directory_path, default = 'img/none.jpg')
	numero_visitas = models.IntegerField(default = 0)

	def __unicode__(self):
		return self.titulo_entrada

	def __str__(self):
		return self.titulo_entrada

	def save(self, *args, **kwargs):
		self.slug_entrada = slugify(self.titulo_entrada)
		super(Entrada, self).save()

class Comentario(models.Model):
	fecha = models.DateField(auto_now = True)
	usuario = models.ForeignKey(User)
	entrada = models.ForeignKey(Entrada)
	comentario_entrada = models.CharField(max_length = 5000)

	def __unicode__(self):
		return self.comentario_entrada

	def __str__(self):
		return self.comentario_entrada