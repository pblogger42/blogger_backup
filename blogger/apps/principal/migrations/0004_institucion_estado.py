# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-07-26 00:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_auto_20170724_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='institucion',
            name='estado',
            field=models.CharField(default='1', max_length=1),
        ),
    ]