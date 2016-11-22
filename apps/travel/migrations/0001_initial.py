# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 21:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=45)),
                ('start_date', models.CharField(max_length=45)),
                ('end_date', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('username', models.CharField(blank=True, max_length=45, null=True)),
                ('email', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='planned_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.Users'),
        ),
    ]