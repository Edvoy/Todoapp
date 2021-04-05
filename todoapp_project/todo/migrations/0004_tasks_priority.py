# Generated by Django 3.1.7 on 2021-04-05 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_tasks_due'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='priority',
            field=models.CharField(choices=[('Low', 'Low'), ('Med', 'Medium'), ('High', 'High'), ('None', 'None')], default='None', max_length=5),
        ),
    ]
