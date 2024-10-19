from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    action = models.CharField(max_length=300, verbose_name='Действие',
                              help_text='Введите действие, которое вы будете выполнять')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель привычки', related_name='habits')
    place = models.CharField(max_length=50, verbose_name='Место',
                             help_text='Введите место в котором необходимо выполнять привычку', **NULLABLE)
    time = models.TimeField(verbose_name='Время',
                            help_text='Введите время в формате ЧЧ:ММ, когда необходимо выполнять привычку')
    is_pleasant_habit = models.BooleanField(default=False, verbose_name='Признак приятной привычки',
                                            help_text='Выберите, если данная привычка является приятной')
    pleasant_habit = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Приятная привычка', **NULLABLE)
    frequency = models.IntegerField(verbose_name='Периодичность выполнения',
                                    help_text='Введите периодичность выполнения привычки для напоминания в днях',
                                    default=1)
    award = models.CharField(max_length=300, verbose_name='Вознаграждение',
                             help_text='Введите вознаграждение за выполнение привычки', **NULLABLE)
    execution_time = models.IntegerField(verbose_name='Время на выполнение',
                                         help_text='Введите время на выполнение привычки в секундах', **NULLABLE)
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности',
                                    help_text='Выберите, если хотите опубликовать свою привычку в общий доступ')
