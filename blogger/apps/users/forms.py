# -*- encoding: utf-8 -*-
from blogger.apps.principal.models import SuscripcionEntrada
from django.forms import *
from django import forms
from .models import *

class PasswordResetRequestForm(forms.Form):
	user_email = forms.CharField(label = 'Digite correo electrónico', widget = forms.EmailInput(attrs = {'class': 'form-control', 'required': True}))

class SetPasswordForm(forms.Form):
	error_messages = {
		'password_mismatch': ("Las contraseñas no coinciden."),
	}
	new_password1 = forms.CharField(label = ("Contraseña nueva"), widget = forms.PasswordInput(attrs = {'class': 'form-control', 'required': True}))
	new_password2 = forms.CharField(label = ("Confirme contraseña"), widget = forms.PasswordInput(attrs = {'class': 'form-control', 'required': True}))

	def clean_new_password2(self):
		password1 = self.cleaned_data.get('new_password1')
		password2 = self.cleaned_data.get('new_password2')
		if password1 != password2:
			raise forms.ValidationError(self.error_messages['password_mismatch'], code = 'error')
		return password2

class UserForm(forms.ModelForm):
	foto_usuario = forms.ImageField(label = 'Foto', required = False)

	class Meta:
		model = User
		fields = ('first_name', 'last_name')
		widgets = {
			'first_name': TextInput(attrs = {'class': 'form-control', 'maxlength': '30', 'required': True}),
			'last_name': TextInput(attrs = {'class': 'form-control', 'maxlength': '30', 'required': True}),
		}
		labels = {
			'first_name': 'Nombres',
			'last_name': 'Apellidos',
		}

	def save(self):
		user = super(UserForm, self).save()
		profile_user = UserProfile.objects.get(user = user)
		if self.cleaned_data['foto_usuario'] is not None:
			profile_user.foto_usuario = self.cleaned_data['foto_usuario']
			profile_user.save()
		return user

class UserSignupForm(forms.ModelForm):
	foto_usuario = forms.ImageField(label = 'Foto')

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email', 'password')
		widgets = {
			'first_name': TextInput(attrs = {'class': 'form-control', 'maxlength': '30', 'required': True}),
			'last_name': TextInput(attrs = {'class': 'form-control', 'maxlength': '30', 'required': True}),
			'email': EmailInput(attrs = {'class': 'form-control', 'maxlength': '30', 'required': True}),
			'password': PasswordInput(attrs = {'class': 'form-control', 'maxlength': '30', 'required': True}),
		}
		labels = {
			'first_name': 'Nombres',
			'last_name': 'Apellidos',
			'email': 'Correo electrónico',
			'password': 'Contraseña',
		}

	def save(self):
		user = super(UserSignupForm, self).save(commit = False)
		user.username = self.cleaned_data['email']
		user.save()
		profile_user = UserProfile(user = user, foto_usuario = self.cleaned_data['foto_usuario'])
		profile_user.save()
		email_suscribe = SuscripcionEntrada(email = self.cleaned_data['email'])
		email_suscribe.save()
		return user

class ChangePasswordForm(forms.Form):
	old_password = forms.CharField(label = 'Contraseña antigua', widget = forms.PasswordInput(attrs = {'class': 'form-control', 'minlength': 8, 'required': True}))
	new_password = forms.CharField(label = 'Contraseña nueva', widget = forms.PasswordInput(attrs = {'class': 'form-control', 'minlength': 8, 'required': True}))
	re_new_password = forms.CharField(label = 'Confirme la contraseña', widget = forms.PasswordInput(attrs = {'class': 'form-control', 'minlength': 8, 'required': True}))