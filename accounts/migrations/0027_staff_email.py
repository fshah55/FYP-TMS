# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2023-11-09 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_remove_staff_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='email',
            field=models.EmailField(max_length=30, null=True),
        ),
    ]
