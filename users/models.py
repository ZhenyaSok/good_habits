from django.contrib.auth.models import AbstractUser
from django.db import models

from habits.models import NULLABLE


class User(AbstractUser):
    """Модель пользователя"""
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    first_name = models.CharField(max_length=50, verbose_name='Имя', **NULLABLE)
    last_name = models.CharField(max_length=75, verbose_name='Фамилия', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='город', **NULLABLE)
    is_active = models.BooleanField(default=False, **NULLABLE)
    last_login = models.DateTimeField(auto_now_add=True, verbose_name='время последнего посещения', **NULLABLE)

    email_verify = models.BooleanField(default=False, verbose_name='проверка почты')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email} - {self.phone}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'




