{% extends "mail_templated/base.tpl" %}

{% block subject %}
	Suscripción a Eri-Acaima
{% endblock %}

{% block html %}
	<div style="background-color: #f5f5f5; padding: 40px 20px; text-align: center;">
		<div style="background-color: white; margin: 0 auto 10px; width: 80%; padding: 20px 20px; border-radius: 5px 5px; box-shadow: 1px 4px 19px -15px rgba(0,0,0,0.75);">
			<h1>Hola,</h1>
			<p>Te has suscrito para recibir correos con articulos recientes publicados por las instituciones en convenio.</p>
		</div>
		<p>Este mensaje ha sido enviado desde <a href="{{ protocol }}{{ domain }}">Blogger</a></p>
		<p><small>¿Deseas salirte de la lista de suscritores? <a href="{{ protocol }}{{ domain }}/unsuscribe/?email={{ args.email }}">Click aquí</a></small></p>
		<p><small>Copyright &copy; 2017. Todos los derechos reservados.</small></p>
	</div>
{% endblock %}