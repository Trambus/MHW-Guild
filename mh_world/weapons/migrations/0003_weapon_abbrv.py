# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weapons', '0002_auto_20171107_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='weapon',
            name='abbrv',
            field=models.CharField(default='wep', max_length=5),
        ),
    ]
