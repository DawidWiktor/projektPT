# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-17 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20170424_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='timestamp',
            field=models.DateField(null=True),
        ),
    ]
