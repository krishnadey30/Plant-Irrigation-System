# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-11 15:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Plants', '0005_auto_20171011_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soil',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name=b'date published'),
        ),
    ]
