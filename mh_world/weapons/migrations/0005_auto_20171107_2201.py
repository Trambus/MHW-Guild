# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 22:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weapons', '0004_bow_chargeblade_greatsword_gunlance_hammer_heavybowgun_huntinghorn_insectglaive_lance_switchaxe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weapon',
            old_name='abbrv',
            new_name='url',
        ),
    ]
