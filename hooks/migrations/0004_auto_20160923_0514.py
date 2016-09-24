# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 05:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hooks', '0003_hook_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='hook',
            name='body2',
            field=models.CharField(max_length=800, null=True),
        ),
        migrations.AddField(
            model_name='hook',
            name='method2',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='hook',
            name='regex2',
            field=models.CharField(default=b'', max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='hook',
            name='url2',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='hook',
            name='body',
            field=models.CharField(max_length=800, null=True),
        ),
    ]
