# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('datamodel', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('bio', models.TextField(max_length=500, blank=True)),
                ('location', models.CharField(max_length=30, blank=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100, blank=True)),
                ('Mobile_no', models.CharField(max_length=15)),
                ('land_ha', models.FloatField(max_length=15, blank=True, null=True)),
                ('soil_type', models.CharField(max_length=15, blank=True, null=True)),
                ('soil_ph', models.FloatField(max_length=10, blank=True, null=True)),
                ('district', models.CharField(max_length=10, blank=True, null=True)),
                ('category', models.CharField(max_length=10, blank=True, null=True)),
                ('yield_tons', models.FloatField(null=True)),
                ('crop1', models.ForeignKey(blank=True, null=True, related_name='crop_2_name', to='datamodel.Crop')),
                ('crop2', models.ForeignKey(blank=True, null=True, related_name='crop_1_Name', to='datamodel.Crop')),
                ('location', models.ForeignKey(to='datamodel.Place')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
