# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-24 04:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('datamodel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('email_confirmed', models.BooleanField(default=False)),
                (
                    'user',
                    models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('Mobile_no', models.CharField(max_length=15)),
                ('land_ha', models.FloatField(blank=True, max_length=15, null=True)),
                ('soil_type', models.CharField(blank=True, max_length=15, null=True)),
                ('soil_ph', models.FloatField(blank=True, max_length=10, null=True)),
                ('district', models.CharField(blank=True, max_length=10, null=True)),
                ('category', models.CharField(blank=True, max_length=10, null=True)),
                ('yield_tons', models.FloatField(null=True)),
                ('crop1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                            related_name='crop_2_name', to='datamodel.Crop')),
                ('crop2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                            related_name='crop_1_Name', to='datamodel.Crop')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datamodel.Place')),
                (
                    'user',
                    models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
