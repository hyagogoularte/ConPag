# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 02:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_auto_20170825_0135'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lancamento',
            options={'ordering': ('data_cadastro', 'titulo')},
        ),
        migrations.RenameField(
            model_name='lancamento',
            old_name='nome',
            new_name='titulo',
        ),
    ]
