# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-18 00:44
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('web_client', '0006_auto_20180217_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawCSVEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.IntegerField()),
                ('weekday', models.CharField(max_length=20)),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField()),
                ('weeks', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z', 32), code='invalid', message='Enter only digits separated by commas.')])),
                ('category', models.TextField(blank=True)),
                ('module', models.TextField(blank=True)),
                ('module_code', models.CharField(blank=True, max_length=10)),
                ('room', models.TextField(blank=True)),
                ('teacher', models.CharField(blank=True, max_length=40)),
                ('group', models.TextField(blank=True, max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='schedulefile',
            name='id',
            field=models.UUIDField(default=uuid.UUID('e226bd62-1444-11e8-8879-20c9d08bb53f'), editable=False, primary_key=True, serialize=False),
        ),
    ]