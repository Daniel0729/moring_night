# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-12 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20161207_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wakeup',
            name='wakeuptime_plan',
            field=models.DateTimeField(),
        ),
    ]
