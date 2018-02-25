{% extends "mail_templated/base.tpl" %}

{% block subject %}
	Suscripción a Eri-Acaima
{% endblock %}

{% load static %}

{% block html %}
	<div style="background-color: #f5f5f5; padding: 40px 20px; text-align: center;">
		<div style="background-color: white; margin: 0 auto 10px; width: 80%; padding: 20px 20px; border-radius: 5px 5px; box-shadow: 1px 4px 19px -15px rgba(0,0,0,0.75); text-align: left;">
			<h1>Hola {{ args.inst_user.user.first_name }} {{ args.inst_user.user.last_name }},</h1>
			<p>El usuario {{ args.escritor.first_name }} {{ args.escritor.last_name }} ha realizado un comentario en la entrada {{ args.entrada.titulo_entrada }}</p>
			<p><a href="{{ protocol }}{{ domain }}{% url 'detalle_entrada' args.entrada.institucion.slug_institucion args.entrada.slug_entrada %}" class="btn btn-primary" style="background-color: #3498db; padding: 10px 10px; border-radius: 3px 3px; color: white; text-decoration: none; margin-bottom: 10px;">Leer comentario</a></p>
		</div>
		<p>Este mensaje ha sido enviado desde <a href="{{ protocol }}{{ domain }}">Blogger</a></p>
		<p><small>Copyright &copy; 2017. Todos los derechos reservados.</small></p>
	</div>
{% endblock %}