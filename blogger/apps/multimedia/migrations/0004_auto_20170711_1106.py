# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-07-11 16:06
from __future__ import unicode_literals

import blogger.apps.multimedia.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multimedia', '0003_auto_20170711_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multimedia',
            name='image_multimedia',
            field=models.ImageField(default='img/none.jpg', upload_to=blogger.apps.multimedia.models.image_directory_path),
        ),
    ]
