# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-15 07:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='WeatherStation',
            fields=[
                ('id', models.CharField(max_length=35, primary_key=True, serialize=False)),
                ('neighborhood', models.CharField(max_length=35)),
            ],
        ),
        migrations.AddField(
            model_name='subscriber',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weather.WeatherStation'),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]