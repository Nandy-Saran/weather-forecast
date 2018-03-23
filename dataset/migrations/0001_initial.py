# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pincode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('pinc', models.CharField(max_length=6)),
                ('place', models.CharField(max_length=25)),
                ('division', models.CharField(max_length=30)),
                ('region', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
            ],
        ),
    ]
