from django.core.exceptions import PermissionDenied
from blogger.apps.users.models import UserProfile
from django.http import HttpResponse

def user_is_entry_author(function):

	def wrap(request, *args, **kwargs):
		if request.user.is_authenticated():
			if UserProfile.objects.filter(institucion__slug_institucion = kwargs['slug'], user = request.user).count() > 0 or request.user.is_superuser:
				return function(request, *args, **kwargs)
		else:
			return HttpResponse(reverse('institucion', kwargs = {'slug': slug}))
	wrap.__doc__ = function.__doc__
	wrap.__name__ = function.__name__
	return wrap