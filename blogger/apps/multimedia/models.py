from __future__ import unicode_literals

from blogger.apps.principal.models import *
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db import models

CHOICE_MULTIMEDIA = (
	('v', 'Video'),
	('f', 'Foto')
)

def image_directory_path(instance, filename):
	return 'img/instituciones/{0}/multimedia/{1}'.format(instance.institucion.slug_institucion, filename)

class Multimedia(models.Model):
	institucion = models.ForeignKey(Institucion)
	nombre_multimedia = models.CharField(max_length = 45)
	slug_multimedia = models.CharField(max_length = 45, blank = True, null = True)
	tipo_multimedia = models.CharField(max_length = 1, choices = CHOICE_MULTIMEDIA)
	image_multimedia = models.ImageField(upload_to = image_directory_path, default = 'img/none.jpg')
	video_multimedia = models.CharField(max_length = 255, blank = True, null = True)

	def __str__(self):
		return self.nombre_multimedia

	def __unicode__(self):
		return self.nombre_multimedia

	def img_resource(self):
		if self.tipo_multimedia == 'v':
			resource = 'https://img.youtube.com/vi/'+self.video_multimedia.split('=')[1]+'/0.jpg'
		else:
			resource = '/static/'+self.image_multimedia.url
		return resource

	def embed_code(self):
		return self.video_multimedia.split('=')[1]

	def url_resource(self):
		return '/static/'+self.image_multimedia.url if self.tipo_multimedia == 'f' else self.video_multimedia

	def save(self, *args, **kwargs):
		self.slug_multimedia = slugify(self.nombre_multimedia)
		super(Multimedia, self).save()

class ComentarioMultimedia(models.Model):
	usuario = models.ForeignKey(User)
	multimedia = models.ForeignKey(Multimedia)
	comentario = models.CharField(max_length = 5000)

	def __str__(self):
		return self.multimedia.slug_multimedia+' - '+self.comentario

	def __unicode__(self):
		return self.multimedia.slug_multimedia+' - '+self.comentario