# Generated by Django 3.0.1 on 2020-01-02 18:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cupApp', '0029_auto_20200102_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='last_visit_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 2, 18, 31, 55, 229961, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='account',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 2, 18, 31, 55, 229961, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='game',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 2, 18, 31, 55, 229961, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='score',
            name='score_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 2, 18, 31, 55, 229961, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 2, 18, 31, 55, 229961, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='submit_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 2, 18, 31, 55, 229961, tzinfo=utc)),
        ),
    ]
