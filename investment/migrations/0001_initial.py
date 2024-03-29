# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2023-11-14 09:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0027_staff_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=30)),
                ('trade_id', models.CharField(max_length=30)),
                ('shares', models.DecimalField(decimal_places=2, max_digits=10)),
                ('spot_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Staff')),
            ],
        ),
    ]
