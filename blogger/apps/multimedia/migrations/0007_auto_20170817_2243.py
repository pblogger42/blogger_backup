# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-08-18 03:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multimedia', '0006_comentariomultimedia_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentariomultimedia',
            name='comentario',
            field=models.CharField(max_length=5000),
        ),
    ]
