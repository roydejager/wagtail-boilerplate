# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-02 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='metaDescription',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]