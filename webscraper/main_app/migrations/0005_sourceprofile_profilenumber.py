# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-24 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20170424_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='sourceprofile',
            name='profileNumber',
            field=models.SmallIntegerField(default=1),
        ),
    ]