# Generated by Django 3.0 on 2019-12-29 12:20

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cupApp', '0027_auto_20191226_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='last_visit_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 29, 12, 20, 49, 882150, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='account',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 29, 12, 20, 49, 881155, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='game',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 29, 12, 20, 49, 882150, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='score',
            name='score_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 29, 12, 20, 49, 883186, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='game_link',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 29, 12, 20, 49, 885168, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='submit_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 29, 12, 20, 49, 885168, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='FavCategory',
            fields=[
                ('favcategoryId', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourite_category', to='cupApp.Category')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favcategory_owner', to='cupApp.Account')),
            ],
        ),
    ]
