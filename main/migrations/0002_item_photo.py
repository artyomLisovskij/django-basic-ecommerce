# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 05:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='photo',
            field=models.ImageField(blank=True, upload_to='/media/'),
        ),
    ]
