# Generated by Django 3.1.7 on 2021-04-11 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0010_tasks_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='priority',
            field=models.CharField(default='', max_length=10),
        ),
    ]