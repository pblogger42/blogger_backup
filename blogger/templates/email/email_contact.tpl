{% extends "mail_templated/base.tpl" %}

{% block subject %}
	Mensaje de contácto
{% endblock %}

{% block html %}
	<div style="background-color: #f5f5f5; padding: 40px 20px; text-align: center;">
		<div style="background-color: white; margin: 0 auto 10px; width: 80%; padding: 20px 20px; border-radius: 5px 5px; box-shadow: 1px 4px 19px -15px rgba(0,0,0,0.75);">
			<h1>Hola {{ args.nombre_admin }},</h1>
			<p>Te ha escrito <b>{{ args.nombre_completo }}</b>:</p>
			<p><b>Número telefónico: </b>{{ args.numero_telefonico }}</p>
			<p><b>Email: </b>{{ args.email }}</p>
			<p><b>Mensaje:</b></p>
			<p>{{ args.mensaje_contact|safe }}</p>
		</div>
		<p>Este mensaje ha sido enviado desde <a href="{{ protocol }}{{ domain }}">Blogger</a></p>
		<small>Copyright &copy; 2017. Todos los derechos reservados.</small>
	</div>
{% endblock %}