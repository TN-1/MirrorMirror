# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-19 12:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_calendaritem_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendaritem',
            name='day',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]
