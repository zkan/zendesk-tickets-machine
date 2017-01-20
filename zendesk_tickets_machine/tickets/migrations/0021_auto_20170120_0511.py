# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-20 05:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0020_ticket_due_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_type',
            field=models.CharField(blank=True, choices=[('question', 'Question'), ('incident', 'Incident'), ('problem', 'Problem'), ('task', 'Task')], max_length=50, null=True),
        ),
    ]
