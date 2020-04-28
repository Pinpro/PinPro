# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-04-28 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200424_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='check',
            field=models.IntegerField(choices=[(0, '未审核'), (1, '已审核'), (2, '未通过审核')], default=0, verbose_name='PIN是否通过审核'),
        ),
    ]