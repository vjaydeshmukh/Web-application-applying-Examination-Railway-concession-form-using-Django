# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-24 09:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0091_examformmodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofilemodel',
            name='roll_no',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
