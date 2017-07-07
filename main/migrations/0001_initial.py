# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommentsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments_body', models.CharField(max_length=150)),
                ('comments_created_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_body', models.CharField(max_length=500)),
                ('post_created_at', models.DateField(auto_now=True)),
            ],
        ),
    ]