# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-22 15:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='nikename',
            new_name='nickname',
        ),
    ]