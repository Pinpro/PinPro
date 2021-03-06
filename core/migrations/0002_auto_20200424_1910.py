# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-04-24 10:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='pin_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pin',
            name='submitter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='pin',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='board',
            name='pins',
            field=models.ManyToManyField(blank=True, related_name='pins', to='core.Pin'),
        ),
        migrations.AddField(
            model_name='board',
            name='submitter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
