from blogger.apps.principal.decorators import user_is_entry_author
from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, url, include
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .views import *

comentario_action_url = [
	url(r'^editar/$', login_required(InstitucionComentarioEditarView.as_view()), name = 'institucion_comentario_editar'),
	url(r'^eliminar/$', login_required(InstitucionComentarioEliminarView.as_view()), name = 'institucion_comentario_eliminar')
]

comentario_url = [
	url(r'^crear/$', login_required(InstitucionComentarioCrearView.as_view()), name = 'institucion_comentario_crear'),
	url(r'^(?P<pk>\d+)/', include(comentario_action_url))
]

entrada_url = [
	url(r'^$', InstitucionEntradaDetalleView.as_view(), name = 'detalle_entrada'),
	url(r'^editar-entrada/$', user_is_entry_author(InstitucionEntradaEditarView.as_view()), name = 'institucion_entrada_editar'),
	url(r'^eliminar-entrada/$', user_is_entry_author(InstitucionEntradaEliminarView.as_view()), name = 'institucion_entrada_eliminar'),
	url(r'^comentario/', include(comentario_url)),
]

urlpatterns = patterns('blogger.apps.entradas.views',
	url(r'^$', InstitucionEntradaView.as_view(), name = 'institucion_entrada'),
	url(r'^crear-entrada/$', user_is_entry_author(InstitucionEntradaCrearView.as_view()), name = 'institucion_entrada_crear'),
	url(r'^(?P<slug_2>[\w-]+)/', include(entrada_url)),
)