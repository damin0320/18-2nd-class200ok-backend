# Generated by Django 3.1.7 on 2021-04-06 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creator',
            name='image_url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='creator',
            name='profile_image_url',
            field=models.URLField(),
        ),
    ]
