# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-05 06:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db1', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
    ]