# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2023-11-05 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_auto_20171113_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='job',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
