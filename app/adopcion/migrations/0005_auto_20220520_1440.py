# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-05-20 14:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0004_auto_20220519_2107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atributovalor',
            old_name='atributo_id',
            new_name='atributo',
        ),
        migrations.RenameField(
            model_name='variaciones',
            old_name='producto_id',
            new_name='producto',
        ),
    ]