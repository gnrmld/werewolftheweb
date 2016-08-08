# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-08 06:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0003_auto_20160805_1517'),
        ('game', '0009_auto_20160808_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turn_description', models.TextField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_log', to='game.Game')),
                ('player', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='game_log', to='player.Player')),
            ],
        ),
    ]