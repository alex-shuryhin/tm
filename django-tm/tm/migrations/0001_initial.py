# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-22 15:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_text', models.CharField(max_length=200)),
                ('goal_t2', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_child', models.CharField(max_length=200)),
                ('plan_aim', models.CharField(max_length=200)),
                ('plan_tree', models.CharField(max_length=200)),
                ('plan_bottleneck', models.CharField(max_length=200)),
                ('plan_wall', models.CharField(max_length=200)),
                ('plan_plank', models.CharField(max_length=200)),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tm.Goal')),
            ],
        ),
    ]
