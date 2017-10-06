# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-06 06:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_name', models.CharField(max_length=200)),
                ('longitude', models.FloatField(default=0)),
                ('latitude', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='soil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moisture', models.FloatField(default=0)),
                ('plant_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Plants.plant')),
            ],
        ),
        migrations.CreateModel(
            name='water_reservoir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water_level', models.FloatField(default=0)),
                ('plant_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Plants.plant')),
            ],
        ),
        migrations.CreateModel(
            name='weather_station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField(default=0)),
                ('humidity', models.FloatField(default=0)),
                ('rainfall', models.FloatField(default=0)),
                ('plant_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Plants.plant')),
            ],
        ),
    ]
