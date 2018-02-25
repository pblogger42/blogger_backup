# -*- encoding: utf-8 -*-
from django.views.generic.edit import FormMixin
from django.core.urlresolvers import reverse
from blogger.apps.principal.emails import *
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import *
from .models import *
from .forms import *

template_dir = 'multimedia/'

class InstitucionMultimediaView(ListView):
	model = Multimedia
	paginate_by = 20
	template_name = template_dir+'lista_multimedia.html'

	def get_context_data(self, **kwargs):
		institucion = Institucion.objects.get(slug_institucion = self.kwargs['slug'])
		context = super(InstitucionMultimediaView, self).get_context_data(**kwargs)
		context['title'] = 'Multimedia'
		context['breadcrumb'] = '<li><a href="'+reverse('institucion', kwargs = {'slug': self.kwargs['slug']})+'">'+institucion.nombre_institucion+'</a></li><li><a href="'+reverse('institucion_multimedia', kwargs = {'slug': self.kwargs['slug']})+'">Multimedia</a></li>'
		context['object'] = institucion
		return context

	def get_queryset(self):
		return super(InstitucionMultimediaView, self).get_queryset().filter(institucion__slug_institucion = self.kwargs['slug']).order_by('-pk')

class InstitucionMultimediaCrearView(CreateView):
	template_name = 'layout/form_general.html'
	success_message = 'Contenido agregado correctamente'
	form_class = MultimediaForm

	def get_context_data(self, **kwargs):
		context = super(InstitucionMultimediaCrearView, self).get_context_data(**kwargs)
		context['title'] = 'Agregar Multimedia'
		context['url'] = reverse('institucion_multimedia_add', kwargs = {'slug': self.kwargs['slug']})
		return context

	def form_valid(self, form):
		form.instance.institucion = Institucion.objects.get(slug_institucion = self.kwargs['slug'])
		form.save()
		return super(InstitucionMultimediaCrearView, self).form_valid(form)

	def get_success_url(self):
		return reverse('institucion_multimedia', kwargs = {'slug': self.kwargs['slug']})

class InstitucionMultimediaDetalleView(FormMixin, ListView):
	model = ComentarioMultimedia
	form_class = MultimediaComentarioForm
	template_name = template_dir+'lista_comentario_multimedia.html'

	def get_context_data(self, **kwargs):
		context = super(InstitucionMultimediaDetalleView, self).get_context_data(**kwargs)
		context['object'] = Multimedia.objects.get(slug_multimedia = self.kwargs['slug_2'])
		return context

	def get_queryset(self):
		return super(InstitucionMultimediaDetalleView, self).get_queryset().filter(multimedia__slug_multimedia = self.kwargs['slug_2'])

	def post(self, request, *args, **kwargs):
		message = 'Ha ocurrido un error, vuelva a intentarlo nuevamente'
		type_message = 'false'
		form =  self.get_form()
		if form.is_valid():
			multimedia = Multimedia.objects.get(slug_multimedia = self.kwargs['slug_2'])
			form.save(form.cleaned_data['comentario'], multimedia, self.request.user)
			for usuario in Institucion.objects.get(slug_institucion = self.kwargs['slug']).userprofile_set.all():
				args = {
					'escritor': self.request.user,
					'inst_user': usuario,
					'multimedia': multimedia
				}
				app_send_email(usuario.user, self.request.META['HTTP_HOST'], 'Nuevo comentario', 'email/email_comentario_multimedia.tpl', args)
			message = 'Comentario realizado'
			type_message = 'true'
		return JsonResponse({'message': message})