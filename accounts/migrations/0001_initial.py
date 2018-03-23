# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-22 20:47
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
                ('email_confirmed', models.BooleanField(default=False)),
                ('mobile', models.CharField(max_length=20)),
                ('land_ha', models.FloatField(blank=True)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('soil_ph', models.FloatField(blank=True, null=True)),
                ('soil_type', models.CharField(blank=True, max_length=20, null=True)),
                ('district', models.CharField(blank=True, max_length=25, null=True)),
                ('category', models.CharField(blank=True, max_length=30, null=True)),
                ('crop1', models.CharField(blank=True, max_length=25, null=True)),
                ('date_of_sow', models.DateField(blank=True, null=True)),
                ('yield_ton', models.FloatField(blank=True, null=True)),
                ('aadhar', models.CharField(max_length=20, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datamodel.Place')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
