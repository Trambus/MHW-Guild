# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 21:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weapons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dualBlades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rarity', models.CharField(max_length=20)),
                ('raw', models.IntegerField()),
                ('element', models.IntegerField()),
                ('elementType', models.CharField(max_length=30)),
                ('status', models.IntegerField()),
                ('statusType', models.CharField(max_length=30)),
                ('affinity', models.IntegerField()),
                ('sharpness', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='lightBowgun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rarity', models.CharField(max_length=20)),
                ('raw', models.IntegerField()),
                ('element', models.IntegerField()),
                ('elementType', models.CharField(max_length=30)),
                ('status', models.IntegerField()),
                ('statusType', models.CharField(max_length=30)),
                ('affinity', models.IntegerField()),
                ('sharpness', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='longsword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rarity', models.CharField(max_length=20)),
                ('raw', models.IntegerField()),
                ('element', models.IntegerField()),
                ('elementType', models.CharField(max_length=30)),
                ('status', models.IntegerField()),
                ('statusType', models.CharField(max_length=30)),
                ('affinity', models.IntegerField()),
                ('sharpness', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='swordShield',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rarity', models.CharField(max_length=20)),
                ('raw', models.IntegerField()),
                ('element', models.IntegerField()),
                ('elementType', models.CharField(max_length=30)),
                ('status', models.IntegerField()),
                ('statusType', models.CharField(max_length=30)),
                ('affinity', models.IntegerField()),
                ('sharpness', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='affinity',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='damage',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='rarity',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='weapon_name',
        ),
        migrations.RemoveField(
            model_name='weapon',
            name='weapon_type',
        ),
        migrations.AddField(
            model_name='weapon',
            name='category',
            field=models.CharField(default='Light', max_length=30),
        ),
        migrations.AddField(
            model_name='weapon',
            name='className',
            field=models.CharField(default='Weapon', max_length=50),
        ),
        migrations.AddField(
            model_name='weapon',
            name='damageType',
            field=models.CharField(default='Cutting', max_length=30),
        ),
        migrations.DeleteModel(
            name='weapon_type',
        ),
        migrations.AddField(
            model_name='swordshield',
            name='weapon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weapons.weapon'),
        ),
        migrations.AddField(
            model_name='longsword',
            name='weapon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weapons.weapon'),
        ),
        migrations.AddField(
            model_name='lightbowgun',
            name='weapon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weapons.weapon'),
        ),
        migrations.AddField(
            model_name='dualblades',
            name='weapon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weapons.weapon'),
        ),
    ]
