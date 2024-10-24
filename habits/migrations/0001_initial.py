# Generated by Django 5.1.2 on 2024-10-19 15:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(help_text='Введите действие, которое вы будете выполнять', max_length=300, verbose_name='Действие')),
                ('place', models.CharField(blank=True, help_text='Введите место в котором необходимо выполнять привычку', max_length=50, null=True, verbose_name='Место')),
                ('time', models.TimeField(help_text='Введите время в формате ЧЧ:ММ, когда необходимо выполнять привычку', verbose_name='Время')),
                ('is_pleasant_habit', models.BooleanField(default=False, help_text='Выберите, если данная привычка является приятной', verbose_name='Признак приятной привычки')),
                ('frequency', models.IntegerField(default=1, help_text='Введите периодичность выполнения привычки для напоминания в днях', verbose_name='Периодичность выполнения')),
                ('award', models.CharField(blank=True, help_text='Введите вознаграждение за выполнение привычки', max_length=300, null=True, verbose_name='Вознаграждение')),
                ('execution_time', models.IntegerField(blank=True, help_text='Введите время на выполнение привычки в секундах', null=True, verbose_name='Время на выполнение')),
                ('is_public', models.BooleanField(default=False, help_text='Выберите, если хотите опубликовать свою привычку в общий доступ', verbose_name='Признак публичности')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habits', to=settings.AUTH_USER_MODEL, verbose_name='Создатель привычки')),
                ('pleasant_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habit', verbose_name='Приятная привычка')),
            ],
        ),
    ]
