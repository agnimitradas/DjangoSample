# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 06:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentsmodel',
            name='comment_on',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='postsModel', to='main.PostsModel'),
            preserve_default=False,
        ),
    ]