# Generated by Django 2.0.5 on 2018-09-11 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_chatstatistics_publicity'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ChatStatistics',
        ),
    ]