# Generated by Django 2.0.5 on 2018-09-11 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_chatstatistics'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ChatStatistics',
            new_name='ChatStats',
        ),
    ]
