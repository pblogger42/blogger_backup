# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-07-06 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entradas', '0003_comentario_comentario_entrada'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='numero_visitas',
            field=models.IntegerField(default=0),
        ),
    ]
