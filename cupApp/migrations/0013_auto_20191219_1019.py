# Generated by Django 3.0 on 2019-12-19 07:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cupApp', '0012_auto_20191219_0955'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='score_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 19, 7, 19, 11, 785138, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_visit_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 19, 7, 19, 11, 785138, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='account',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 19, 7, 19, 11, 785138, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='game',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 19, 7, 19, 11, 785138, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 19, 7, 19, 11, 794940, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='submit_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 19, 7, 19, 11, 794940, tzinfo=utc)),
        ),
    ]