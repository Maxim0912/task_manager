# Generated by Django 3.0.5 on 2020-10-01 11:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='planned_finish_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Планируемое время завершения'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 1, 11, 52, 51, 288112), verbose_name='Время создания'),
        ),
    ]
