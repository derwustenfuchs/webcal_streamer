# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-18 01:43
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('web_client', '0009_auto_20180218_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulefile',
            name='id',
            field=models.UUIDField(default=uuid.UUID('22f74328-144d-11e8-9d51-20c9d08bb53f'), editable=False, primary_key=True, serialize=False),
        ),
    ]
