# Generated by Django 4.0.3 on 2022-05-16 22:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_rename_aboutme_shopuserprofile_about_me_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 18, 22, 56, 46, 245967, tzinfo=utc)),
        ),
    ]
