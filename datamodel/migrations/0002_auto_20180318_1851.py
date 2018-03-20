# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datamodel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather',
            name='WindDesc',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AddField(
            model_name='weather',
            name='WindDirdeg',
            field=models.CharField(max_length=30, default=''),
        ),
        migrations.AddField(
            model_name='weather',
            name='Winddir16Point',
            field=models.CharField(max_length=30, default=''),
            preserve_default=False,
        ),
    ]
