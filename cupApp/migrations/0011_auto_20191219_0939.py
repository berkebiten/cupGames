# Generated by Django 3.0 on 2019-12-19 06:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cupApp', '0010_auto_20191219_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestion',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 19, 6, 39, 58, 531999, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='submit_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 19, 6, 39, 58, 531999, tzinfo=utc)),
        ),
    ]
