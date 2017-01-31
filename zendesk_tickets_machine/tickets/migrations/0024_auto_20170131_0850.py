# -*- coding: utf-8 -*-
# Generated by Django 1.11a1 on 2017-01-31 08:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0001_initial'),
        ('tickets', '0023_ticket_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to='agents.Agent'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='assignee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignee', to='agents.Agent'),
        ),
    ]
