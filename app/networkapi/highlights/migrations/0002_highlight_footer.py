# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-13 21:33
from __future__ import unicode_literals

from django.db import migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('highlights', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='highlight',
            name='footer',
            field=mezzanine.core.fields.RichTextField(help_text='Content to appear after description (view more projects link or something similar)', null=True, verbose_name='footer'),
        ),
    ]
