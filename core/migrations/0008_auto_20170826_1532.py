# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0007_auto_20170826_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lancamento',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=25),
        ),
    ]
