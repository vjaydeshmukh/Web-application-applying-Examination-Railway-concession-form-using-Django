# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-15 08:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0064_auto_20190415_0821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atktmodel',
            name='current_year',
        ),
        migrations.RemoveField(
            model_name='atktmodel',
            name='semister',
        ),
        migrations.AddField(
            model_name='atktmodel',
            name='semester',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.Semester'),
        ),
        migrations.AddField(
            model_name='atktmodel',
            name='subject',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='atktmodel',
            name='year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.Year'),
        ),
        migrations.AlterField(
            model_name='atktmodel',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.Branch'),
        ),
    ]