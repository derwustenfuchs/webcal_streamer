# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-18 00:51
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('web_client', '0007_auto_20180218_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawcsvevent',
            name='ref',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='schedulefile',
            name='id',
            field=models.UUIDField(default=uuid.UUID('e889577a-1445-11e8-9535-20c9d08bb53f'), editable=False, primary_key=True, serialize=False),
        ),
    ]
