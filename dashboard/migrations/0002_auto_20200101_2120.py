# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-01 13:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='idc',
            table='dashboard_idc',
        ),
    ]
