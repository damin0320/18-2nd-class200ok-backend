# Generated by Django 3.1.7 on 2021-03-31 08:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pendinglecture',
            name='vote_by',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 15, 8, 21, 49, 975919)),
        ),
    ]
