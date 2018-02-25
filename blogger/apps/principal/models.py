from __future__ import unicode_literals

# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db import models

CHOICE_ESTADO = (
	('1', 'Activo'),
	('2', 'Inactivo')
)

def image_directory_path(instance, filename):
	return 'img/instituciones/{0}/{1}'.format(instance.slug_institucion, filename)

class Institucion(models.Model):
	nombre_institucion = models.CharField(max_length = 50)
	slug_institucion = models.SlugField(max_length = 80, unique = True, blank = True, null = True)
	logo_institucion = models.ImageField(upload_to = image_directory_path)
	image_back_institucion = models.ImageField(upload_to = image_directory_path)
	descripcion_institucion = models.CharField(max_length = 10000)
	estado = models.CharField(max_length = 1, default = '1', choices = CHOICE_ESTADO)

	def __str__(self):
		return self.nombre_institucion

	def __unicode__(self):
		return self.nombre_institucion

	def save(self, *args, **kwargs):
		self.slug_institucion = slugify(self.nombre_institucion)
		super(Institucion, self).save()

class SuscripcionEntrada(models.Model):
	email = models.EmailField()
	fecha_suscripcion = models.DateField(auto_now = True)

	def __str__(self):
		return self.email

	def __unicode__(self):
		return self.email

class Slider(models.Model):
	foto = models.ImageField(upload_to = 'img/')
	titulo = models.CharField(max_length = 50)

	def __str__(self):
		return self.titulo

	def __unicode__(self):
		return self.titulo

class InstitucionSlider(models.Model):
	institucion = models.ForeignKey(Institucion)
	foto = models.ImageField(upload_to = image_directory_path)