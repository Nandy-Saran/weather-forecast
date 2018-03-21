# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100, blank=True)),
                ('Mobile_no', models.CharField(max_length=15)),
                ('land_ha', models.FloatField(max_length=15, blank=True, null=True)),
                ('soil_type', models.CharField(max_length=15, blank=True)),
                ('soil_ph', models.FloatField(max_length=10, blank=True)),
                ('district', models.CharField(max_length=10, blank=True)),
                ('sub_district', models.CharField(max_length=10, blank=True)),
                ('category', models.CharField(max_length=10, blank=True)),
                ('yield_tons', models.FloatField()),
                ('crop1', models.CharField(max_length=30, blank=True)),
                ('crop2', models.CharField(max_length=30, blank=True)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
