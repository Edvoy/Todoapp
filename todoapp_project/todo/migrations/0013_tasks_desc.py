# Generated by Django 3.1.7 on 2021-04-11 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0012_auto_20210411_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='desc',
            field=models.CharField(default='', max_length=500),
        ),
    ]
