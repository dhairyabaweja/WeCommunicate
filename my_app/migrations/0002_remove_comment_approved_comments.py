# Generated by Django 2.0.7 on 2018-07-13 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved_comments',
        ),
    ]
