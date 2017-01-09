# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='content',
            field=models.CharField(max_length=1048576, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookmark',
            name='title',
            field=models.CharField(max_length=128, default=''),
            preserve_default=False,
        ),
    ]
