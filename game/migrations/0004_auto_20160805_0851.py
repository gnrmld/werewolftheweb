# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-05 00:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20160804_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='ip',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]