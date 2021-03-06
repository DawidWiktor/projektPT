# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-20 11:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20170419_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlesourcemap',
            name='ArticleID',
        ),
        migrations.RemoveField(
            model_name='articlesourcemap',
            name='SourceID',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='Source',
        ),
        migrations.AddField(
            model_name='articles',
            name='SourceID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='data.Sources'),
        ),
        migrations.AlterField(
            model_name='sources',
            name='Name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.DeleteModel(
            name='ArticleSourceMap',
        ),
    ]
