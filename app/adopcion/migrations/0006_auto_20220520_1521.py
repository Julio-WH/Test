# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-05-20 15:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0005_auto_20220520_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atributovalor',
            name='atributo',
        ),
        migrations.RemoveField(
            model_name='variaciones',
            name='atributos',
        ),
        migrations.RemoveField(
            model_name='variaciones',
            name='producto',
        ),
        migrations.DeleteModel(
            name='Atributo',
        ),
        migrations.DeleteModel(
            name='AtributoValor',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
        migrations.DeleteModel(
            name='Variaciones',
        ),
    ]