# Generated by Django 3.0.5 on 2020-10-07 08:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20201001_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 7, 8, 0, 16, 772986), verbose_name='Время создания'),
        ),
    ]