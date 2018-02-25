# -*- encoding: utf-8 -*-
from django.forms import *
from django import forms
from .models import *

class EntradaForm(forms.ModelForm):
	class Meta:
		model = Entrada
		fields = '__all__'
		exclude = ('institucion', 'usuario', 'fecha_actualizacion_entrada', 'slug_entrada', 'numero_visitas')
		widgets = {
			'titulo_entrada': TextInput(attrs = {'class': 'form-control', 'maxlength': '50', 'required': True}),
			'descripcion_entrada': Textarea(attrs = {'class': 'textarea'}),
		}
		labels = {
			'titulo_entrada': 'Título',
			'descripcion_entrada': 'Descripción',
			'imagen_portada': 'Imagen portada'
		}

class ComentarioForm(forms.ModelForm):
	class Meta:
		model = Comentario
		fields = '__all__'
		exclude = ('entrada', 'usuario')
		widgets = {
			'comentario_entrada': Textarea(attrs = {'class': 'textarea'}),
		}
		labels = {
			'comentario_entrada': 'Comentario'
		}