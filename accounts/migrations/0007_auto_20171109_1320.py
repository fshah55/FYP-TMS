# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20171109_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.TextField(max_length=80),
        ),
    ]
