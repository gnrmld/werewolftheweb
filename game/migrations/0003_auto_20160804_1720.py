# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-04 09:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_players'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Players',
            new_name='Player',
        ),
    ]