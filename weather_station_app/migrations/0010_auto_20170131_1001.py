# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-31 09:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weather_station_app', '0009_auto_20170126_1905'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldEncoding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_no', models.PositiveSmallIntegerField()),
                ('encoding', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='channel',
            name='number_fields',
            field=models.PositiveSmallIntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='field',
            name='field_no',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='field',
            name='value',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='fieldencoding',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather_station_app.Channel'),
        ),
    ]
