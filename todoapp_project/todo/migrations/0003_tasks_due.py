# Generated by Django 3.1.7 on 2021-04-05 09:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20210405_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='due',
            field=models.DateField(default=datetime.date.today),
        ),
    ]