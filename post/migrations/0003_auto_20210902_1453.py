# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-09-02 11:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20210902_1356'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='cathPhrase',
            new_name='catch_phrase',
        ),
    ]