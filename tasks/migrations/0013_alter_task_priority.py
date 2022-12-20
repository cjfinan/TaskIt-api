# Generated by Django 3.2.16 on 2022-12-19 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_alter_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[(3, 'HIGH'), (2, 'Medium'), (1, 'Low')], default='Medium', max_length=50),
        ),
    ]