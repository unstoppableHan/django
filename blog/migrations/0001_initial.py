# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-08 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortName', models.CharField(max_length=50)),
                ('fullName', models.CharField(max_length=50)),
                ('homePage', models.CharField(max_length=200)),
            ],
        ),
    ]
