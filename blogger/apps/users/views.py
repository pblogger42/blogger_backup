# -*- encoding: utf-8 -*-
from django.contrib.auth.tokens import default_token_generator
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from blogger.apps.principal.emails import *
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import *
from .forms import *
import json

var_dir_template = 'usuario/'

class ResetPasswordRequestView(FormView):
	template_name = var_dir_template+'form_password_reset_email.html'
	success_url = reverse_lazy('login')
	form_class = PasswordResetRequestForm

	def get_context_data(self, **kwargs):
		context = super(ResetPasswordRequestView, self).get_context_data(**kwargs)
		context['title'] = 'Recuperación de cuenta'
		return context

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			user_email = form.cleaned_data["user_email"].lower()
			try:
				user = User.objects.get(email = user_email)
				app_send_email(user, request.META['HTTP_HOST'], 'Cambio de Contraseña', 'email/password_reset_subject.tpl', '')
				result = self.form_valid(form)
				messages.success(request, 'Un correo ha sido enviado ha ' +user_email+". Por favor verifica tu correo y sigue las instrucciones.")
			except User.DoesNotExist:
				result = self.form_invalid(form)
				messages.warning(request, 'No hay una cuenta asociada con el correo electronico digitado.')
		return result

class PasswordResetConfirmView(FormView):
	template_name = var_dir_template+'form_password_reset_email.html'
	success_url = reverse_lazy('login')
	form_class = SetPasswordForm

	def get_context_data(self, **kwargs):
		context = super(PasswordResetConfirmView, self).get_context_data(**kwargs)
		context['title'] = 'Recuperación de cuenta'
		return context

	@staticmethod
	def validate_url(uidb64, token):
		UserModel = get_user_model()
		assert uidb64 is not None and token is not None
		try:
			uid = urlsafe_base64_decode(uidb64)
			user = UserModel._default_manager.get(pk = uid)
		except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
			user = None
		return user

	def post(self, request, uidb64 = None, token = None, *arg, **kwargs):
		user = self.validate_url(uidb64, token)
		form = self.form_class(request.POST)
		if user is not None and default_token_generator.check_token(user, token):
			if form.is_valid():
				new_password = form.cleaned_data['new_password2']
				user.set_password(new_password)
				user.save()
				messages.success(request, 'Cambio de contraseña exitoso.')
				return self.form_valid(form)
			else:
				messages.warning(request, 'Ha ocurrido un error.')
				return self.form_invalid(form)
		else:
			messages.warning(request, 'La URL no es válida.')
			return HttpResponseRedirect(reverse('login'))

class UserRegistrateView(SuccessMessageMixin, FormView):
	template_name = var_dir_template+'form_registrate.html'
	success_message = 'Gracias por registrarse en Eri-Acaima.'
	success_url = reverse_lazy('login')
	form_class = UserSignupForm

	def get_context_data(self, **kwargs):
		context = super(UserRegistrateView, self).get_context_data(**kwargs)
		context['title'] = 'Registrate en Eri-Acaima'
		return context

	def form_valid(self, form):
		form.save()
		return super(UserRegistrateView, self).form_valid(form)

class PerfilUsuarioView(SuccessMessageMixin, UpdateView):
	model = User
	template_name = var_dir_template+'perfil.html'
	success_message = 'Usuario actualizado correctamente'
	success_url = reverse_lazy('perfil')
	form_class = UserForm

	def get_context_data(self, **kwargs):
		context = super(PerfilUsuarioView, self).get_context_data(**kwargs)
		context['title'] = 'Mi perfil'
		return context

	def form_valid(self, form):
		form.save()
		return super(PerfilUsuarioView, self).form_valid(form)

	def get_object(self, queryset = None):
		return self.request.user

def change_password(request):
	if request.method == 'POST':
		response = {}
		form = ChangePasswordForm(request.POST)
		if form.is_valid():
			old_password = form.cleaned_data['old_password']
			new_password = form.cleaned_data['new_password']
			re_new_password = form.cleaned_data['re_new_password']
			if new_password == re_new_password:
				saveuser = User.objects.get(pk = request.user.pk)
				if request.user.check_password(old_password):
					saveuser.set_password(new_password);
					saveuser.save()
					response['type'] = 'success'
					response['msg'] = 'Cambio de contraseña exitoso.'
				else:
					response['type'] = 'error'
					response['msg'] = 'Contraseña antigua errónea.'
			else:
				response['type'] = 'error'
				response['msg'] = 'Contraseñas no coinciden.'
		return HttpResponse(json.dumps(response), "application/json")
	else:
		form = ChangePasswordForm()
	return render(request, var_dir_template+'form_password.html', {'forms': form, 'title': 'Cambiar mi contraseña'})