# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-16 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_auto_20180716_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='static/profilePic'),
        ),
    ]