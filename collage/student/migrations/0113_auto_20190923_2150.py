# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-09-23 16:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0112_remove_examformmodel_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atktmodel',
            name='subject1',
        ),
        migrations.RemoveField(
            model_name='atktmodel',
            name='subject2',
        ),
        migrations.RemoveField(
            model_name='atktmodel',
            name='subject3',
        ),
        migrations.RemoveField(
            model_name='atktmodel',
            name='subject4',
        ),
        migrations.RemoveField(
            model_name='atktmodel',
            name='subject5',
        ),
        migrations.RemoveField(
            model_name='atktmodel',
            name='subject6',
        ),
        migrations.RemoveField(
            model_name='atktphotocopymodel',
            name='subject1',
        ),
        migrations.RemoveField(
            model_name='atktphotocopymodel',
            name='subject2',
        ),
        migrations.RemoveField(
            model_name='atktphotocopymodel',
            name='subject3',
        ),
        migrations.RemoveField(
            model_name='atktphotocopymodel',
            name='subject4',
        ),
        migrations.RemoveField(
            model_name='atktphotocopymodel',
            name='subject5',
        ),
        migrations.RemoveField(
            model_name='atktphotocopymodel',
            name='subject6',
        ),
        migrations.RemoveField(
            model_name='atktrevalutionmodel',
            name='subject1',
        ),
        migrations.RemoveField(
            model_name='atktrevalutionmodel',
            name='subject2',
        ),
        migrations.RemoveField(
            model_name='atktrevalutionmodel',
            name='subject3',
        ),
        migrations.RemoveField(
            model_name='atktrevalutionmodel',
            name='subject4',
        ),
        migrations.RemoveField(
            model_name='atktrevalutionmodel',
            name='subject5',
        ),
        migrations.RemoveField(
            model_name='atktrevalutionmodel',
            name='subject6',
        ),
        migrations.RemoveField(
            model_name='regularphotocopymodel',
            name='subject1',
        ),
        migrations.RemoveField(
            model_name='regularphotocopymodel',
            name='subject2',
        ),
        migrations.RemoveField(
            model_name='regularphotocopymodel',
            name='subject3',
        ),
        migrations.RemoveField(
            model_name='regularphotocopymodel',
            name='subject4',
        ),
        migrations.RemoveField(
            model_name='regularphotocopymodel',
            name='subject5',
        ),
        migrations.RemoveField(
            model_name='regularphotocopymodel',
            name='subject6',
        ),
        migrations.RemoveField(
            model_name='regularrevalutionmodel',
            name='subject1',
        ),
        migrations.RemoveField(
            model_name='regularrevalutionmodel',
            name='subject2',
        ),
        migrations.RemoveField(
            model_name='regularrevalutionmodel',
            name='subject3',
        ),
        migrations.RemoveField(
            model_name='regularrevalutionmodel',
            name='subject4',
        ),
        migrations.RemoveField(
            model_name='regularrevalutionmodel',
            name='subject5',
        ),
        migrations.RemoveField(
            model_name='regularrevalutionmodel',
            name='subject6',
        ),
    ]