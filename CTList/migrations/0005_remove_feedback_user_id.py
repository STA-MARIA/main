# Generated by Django 3.1.6 on 2022-07-01 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CTList', '0004_auto_20220701_0500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='User_ID',
        ),
    ]
