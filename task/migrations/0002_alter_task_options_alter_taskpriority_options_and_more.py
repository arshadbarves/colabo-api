# Generated by Django 5.0.3 on 2024-03-24 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['due_date'], 'verbose_name_plural': 'Tasks'},
        ),
        migrations.AlterModelOptions(
            name='taskpriority',
            options={'verbose_name_plural': 'Task priorities'},
        ),
        migrations.AlterModelOptions(
            name='taskstatus',
            options={'verbose_name_plural': 'Task statuses'},
        ),
    ]
