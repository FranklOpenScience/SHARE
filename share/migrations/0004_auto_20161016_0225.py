# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-16 02:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0003_update_trigger_migrations_20161016_0158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='normalizeddata',
            old_name='normalized_data',
            new_name='data',
        ),
    ]
