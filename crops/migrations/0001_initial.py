# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-19 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='crop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('season', models.CharField(max_length=200)),
                ('season_num', models.CharField(max_length=50)),
                ('comments', models.CharField(max_length=200)),
                ('min_temp', models.IntegerField()),
                ('max_temp', models.IntegerField()),
                ('fertilizer', models.CharField(max_length=50)),
                ('flower_init', models.CharField(max_length=50)),
                ('first_picking', models.CharField(max_length=100)),
                ('growth_regulatore', models.TimeField()),
                ('yield_crops', models.CharField(max_length=60)),
                ('no_of_pickings', models.CharField(max_length=60)),
                ('date_of_pickings', models.CharField(max_length=60)),
                ('gap', models.IntegerField()),
                ('Count', models.IntegerField()),
            ],
        ),
    ]
