# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-21 13:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0002_auto_20171021_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grupos',
            name='reuniao_meio',
        ),
    ]
