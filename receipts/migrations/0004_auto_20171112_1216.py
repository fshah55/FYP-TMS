# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipts', '0003_auto_20171112_0921'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='total_mount',
            new_name='total_cost',
        ),
        migrations.RemoveField(
            model_name='receipt',
            name='remarks',
        ),
        migrations.AddField(
            model_name='receipt',
            name='notes',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='address',
            field=models.CharField(max_length=80),
        ),
    ]
