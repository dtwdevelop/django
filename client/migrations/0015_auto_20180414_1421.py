# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-14 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0014_auto_20171130_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='created',
            field=models.DateTimeField(null=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='client',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
