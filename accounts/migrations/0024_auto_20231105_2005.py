# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2023-11-05 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_staff_borrow'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='dues',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='lend',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
