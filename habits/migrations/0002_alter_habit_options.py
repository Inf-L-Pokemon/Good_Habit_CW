# Generated by Django 5.1.2 on 2024-10-19 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='habit',
            options={'verbose_name': 'Привычка', 'verbose_name_plural': 'Привычки'},
        ),
    ]
