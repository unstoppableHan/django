# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-08 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_cryptomodel_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='cryptomodel',
            name='altorithm',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
