# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-24 14:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0092_userprofilemodel_roll_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='atktmodel',
            name='amount',
            field=models.IntegerField(choices=[(1, '200'), (2, '400'), (3, '600'), (4, '800'), (5, '800'), (6, '950')], default=6),
        ),
    ]
