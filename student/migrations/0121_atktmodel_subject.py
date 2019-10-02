# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-09-24 17:31
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0120_auto_20190924_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='atktmodel',
            name='subject',
            field=multiselectfield.db.fields.MultiSelectField(choices=[['Applied Mathmatics III', 'Applied Mathmatics III'], ['Database Management System', 'Database Management System'], ['Data Structure & Algorithm', 'Data Structure & Algorithm'], ['Object Oriented Programming', 'Object Oriented Programming'], ['Principles of Analog & Digital', 'Principles of Analog & Digital']], max_length=135, null=True),
        ),
    ]