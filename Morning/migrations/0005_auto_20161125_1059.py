# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-25 15:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Morning', '0004_auto_20161125_1057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mlight_state',
            old_name='Mlight',
            new_name='light',
        ),
    ]