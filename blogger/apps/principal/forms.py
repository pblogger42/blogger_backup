# -*- encoding: utf-8 -*-
from blogger.apps.users.models import UserProfile
from mail_templated import send_mail
from .tasks import send_email_task
from django.conf import settings
from django.forms import *
from django import forms
from .models import *

class ContactForm(forms.Form):
	fullname = forms.CharField(label = 'Nombre completo', widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Digite el nombre completo'}))
	cellphone = forms.CharField(label = 'Número telefónico', widget = forms.TextInput(attrs = {'class': 'form-control only-number', 'placeholder': 'Digite el número telefónico'}))
	email = forms.CharField(label = 'Email', widget = forms.EmailInput(attrs = {'class': 'form-control', 'placeholder': 'Digite el correo electrónico'}))
	mensaje = forms.CharField(label = 'Mensaje', widget = forms.Textarea())

	def send_email(self, slug_institucion, request):
		institucion = Institucion.objects.get(slug_institucion = slug_institucion)
		for users in institucion.userprofile_set.all():
			args = {
				'nombre_admin': users.user.first_name+' '+users.user.last_name,
				'email': self.cleaned_data['email'],
				'nombre_completo': self.cleaned_data['fullname'],
				'numero_telefonico': self.cleaned_data['cellphone'],
				'mensaje_contact': self.cleaned_data['mensaje']
			}
			send_email_task.delay('email/email_contact.tpl', users.user.email, request, 'Contácto', args)

class SuscribeForm(forms.Form):
	email = forms.CharField(label = 'Email', widget = forms.EmailInput(attrs = {'class': 'form-control', 'placeholder': 'Digite el correo electrónico'}))

	def suscribe(self, request):
		email = self.cleaned_data['email']
		if not SuscripcionEntrada.objects.filter(email = email).exists():
			send_email_task.delay('email/email_suscriber.tpl', email, request, 'Suscripción a Eri-Acaima', {'email': self.cleaned_data['email']})
			email_suscribe = SuscripcionEntrada(email = email)
			email_suscribe.save()

class InstitucionUsuarioForm(forms.Form):
	usuario = forms.ChoiceField(label = 'Usuario', widget = forms.Select(attrs = {'class': 'form-control'}))

	def save(self, slug_institucion):
		user_profile = UserProfile.objects.get(pk = self.cleaned_data['usuario'])
		user_profile.institucion = Institucion.objects.get(slug_institucion = slug_institucion)
		user_profile.save()

	def __init__(self, *args, **kwargs):
		super(InstitucionUsuarioForm, self).__init__(*args, **kwargs)
		self.fields['usuario'].choices = [('', 'Seleccione un usuario')]+[(x.pk, x.user.first_name+' '+x.user.last_name) for x in UserProfile.objects.filter(institucion = None)]

class InstitucionForm(forms.ModelForm):
	class Meta:
		model = Institucion
		fields = '__all__'
		exclude = ('slug_institucion', '')
		widgets = {
			'nombre_institucion': TextInput(attrs = {'class': 'form-control', 'maxlength': '50', 'required': True}),
			'descripcion_institucion': Textarea(attrs = {'class': 'textarea'})
		}
		labels = {
			'nombre_institucion': 'Nombre institución',
			'logo_institucion': 'Logo institución',
			'descripcion_institucion': 'Descripción de la institución',
			'image_back_institucion': 'Imagen portada'
		}

	def __init__(self, *args, **kwargs):
		super(InstitucionForm, self).__init__(*args, **kwargs)
		self.fields['estado'].widget.attrs = {'class': 'form-control'}
		self.fields['logo_institucion'].widget.attrs = {'accept': '.jpg,.png,.jpeg'}
		self.fields['image_back_institucion'].widget.attrs = {'accept': '.jpg,.png,.jpeg'}
