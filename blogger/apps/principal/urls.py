from blogger.apps.principal.decorators import user_is_entry_author
from django.conf.urls import patterns, url, include
from .views import *

usuarios_institucion = [
	url(r'^$', user_is_entry_author(InstitucionUsuarioView.as_view()), name = 'institucion_usuario'),
	url(r'^agregar/$', user_is_entry_author(InstitucionUsuarioAddView.as_view()), name = 'institucion_usuario_add'),
	url(r'^delete/(?P<pk_userprofile>\d+)/$', user_is_entry_author(InstitucionUsuarioDeleteView), name = 'delete_usuario_institucion'),
]

pagina_institucion = [
	url(r'^acerca-de/$', InstitucionView.as_view(), name = 'institucion'),
	url(r'^contacto/$', InstitucionContactoView.as_view(), name = 'institucion_contacto'),
	url(r'^multimedia/', include('blogger.apps.multimedia.urls')),
	url(r'^usuarios/', include(usuarios_institucion)),
	url(r'^editar/$', InstitucionEditarView.as_view(), name = 'institucion_editar'),
	url(r'^', include('blogger.apps.entradas.urls')),
]

urlpatterns = patterns('blogger.apps.principal.views',
	url(r'^$', InicioTemplateView.as_view(), name = 'inicio'),
	url(r'^unsuscribe/$', 'unsuscribe_email', name = 'unsuscribe_email'),
	url(r'^suscribe/$', SuscribeView.as_view(), name = 'suscribe_email'),
	url(r'^nueva-institucion/$', InstitucionCreateView.as_view(), name = 'institucion_crear'),
	url(r'^(?P<slug>[\w-]+)/', include(pagina_institucion)),
)