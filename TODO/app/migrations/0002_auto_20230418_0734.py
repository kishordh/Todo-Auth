# Generated by Django 3.1.2 on 2023-04-18 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='status_choices',
            new_name='status',
        ),
    ]
