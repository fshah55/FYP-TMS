# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-13 05:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receipts', '0009_receipt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipt',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='receipt',
            name='items',
        ),
        migrations.DeleteModel(
            name='Receipt',
        ),
    ]
