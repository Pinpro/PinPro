# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-04-29 05:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200424_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='gender',
            field=models.SmallIntegerField(choices=[(0, ''), (1, '男♂'), (2, '女♀'), (3, '⚧')], default='0', verbose_name='性别'),
        ),
    ]