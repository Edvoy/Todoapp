# Generated by Django 3.1.7 on 2021-04-08 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_auto_20210407_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='project',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='desc',
            field=models.CharField(default='', max_length=500),
        ),
    ]
