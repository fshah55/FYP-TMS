# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2023-11-05 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_staff_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='borrow',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
