# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 06:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_commentsmodel_comment_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='postsmodel',
            name='post_created_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
