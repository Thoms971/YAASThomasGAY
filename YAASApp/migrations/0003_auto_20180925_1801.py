# Generated by Django 2.1.1 on 2018-09-25 15:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YAASApp', '0002_auto_20180923_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 26, 18, 1, 46, 609946)),
        ),
    ]