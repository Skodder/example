# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-09-02 10:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addres',
            options={'verbose_name': 'Адрес', 'verbose_name_plural': 'Адреса'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Компания', 'verbose_name_plural': 'Компании'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Персона', 'verbose_name_plural': 'Персоны'},
        ),
    ]