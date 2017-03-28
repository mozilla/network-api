# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-28 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20170327_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='excerpt',
            field=models.TextField(blank=True, help_text='A small extract from the article', max_length=1000, null=True),
        ),
    ]
