# Generated by Django 2.0.5 on 2018-09-11 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_delete_chatstatistics'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Topic', models.CharField(max_length=50)),
                ('Number', models.IntegerField(default=0)),
                ('Admin', models.CharField(max_length=30)),
            ],
        ),
    ]
