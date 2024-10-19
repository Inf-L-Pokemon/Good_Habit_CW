from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email', help_text='Введите вашу существующую почту')

    city = models.CharField(max_length=50, verbose_name='Город', help_text='Название города в котором живете',
                            **NULLABLE)
    avatar = models.ImageField(upload_to='users/avatars/', verbose_name='Аватар', help_text='Загрузите аватар',
                               **NULLABLE)
    tg_chat_id = models.CharField(max_length=20, verbose_name='Телеграмм chat_id',
                                  help_text='Введите свой chat_id из Телеграмм', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
