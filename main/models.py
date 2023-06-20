from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    username = models.CharField(verbose_name='Логин', blank=False, max_length=40, unique=True)
    name = models.CharField(verbose_name='Имя', blank=False, max_length=40)
    surename = models.CharField(verbose_name='Фамилия', blank=False, max_length=40)
    password = models.CharField(verbose_name='Пароль', blank=False, max_length=40)
    patronymic = models.CharField(verbose_name='Отчество', blank=True, max_length=40)
    email = models.EmailField(verbose_name='Почта', blank=False, max_length=40)

    USERNAME_FIELD = 'username'


class Product(models.Model):
    name = models.CharField(verbose_name='Название', blank=False, max_length=40)
    image = models.ImageField(verbose_name='Изображение', blank=False, upload_to='static/main/img')
    price = models.DecimalField(verbose_name='Цена', blank=False, max_digits=10, decimal_places=2)
    country = models.CharField(verbose_name='Страна производитель', blank=True, max_length=40)
    year = models.IntegerField(verbose_name='Год производства', blank=False)
    model = models.CharField(verbose_name='Модель', blank=True, max_length=40)
    count = models.IntegerField(verbose_name='Количество', blank=False, default=1)


class Worker(models.Model):
    name = models.CharField(verbose_name='ФИО', blank=False, max_length=60)
    post = models.CharField(verbose_name='Должность', blank=False, max_length=80)
    image = models.ImageField(verbose_name='Фото', blank=False, upload_to='static/main/img')
    description = models.CharField(verbose_name='Характеристика', blank=True, max_length=60)
    experience = models.IntegerField(verbose_name='Стаж', blank=False)

    def __str__(self):
        return self.name


class Form(models.Model):
    name = models.CharField(verbose_name='Имя', blank=False, max_length=60)
    number = models.IntegerField(verbose_name='Номер телефона', blank=False)
    email = models.EmailField(verbose_name='Почта', blank=False, max_length=40)
    message = models.CharField(verbose_name='Сообщение', blank=False, max_length=300)

    def __str__(self):
        return self.email


class Review(models.Model):
    name = models.CharField(verbose_name='Имя', blank=False, max_length=60)
    comment = models.CharField(verbose_name='Коментарий', blank=False, max_length=3000)
    date = models.DateTimeField(verbose_name='Дата комментария', blank=True, default=timezone.now)


class Portfolio(models.Model):
    name = models.CharField(verbose_name='Название', blank=False, max_length=100)
    image_1 = models.ImageField(verbose_name='Изображение', blank=False, upload_to='static/main/img')
    image_2 = models.ImageField(verbose_name='Изображение', blank=True, upload_to='static/main/img')
    image_3 = models.ImageField(verbose_name='Изображение', blank=True, upload_to='static/main/img')
    image_4 = models.ImageField(verbose_name='Изображение', blank=True, upload_to='static/main/img')
    image_5 = models.ImageField(verbose_name='Изображение', blank=True, upload_to='static/main/img')
    image_6 = models.ImageField(verbose_name='Изображение', blank=True, upload_to='static/main/img')
    image_7 = models.ImageField(verbose_name='Изображение', blank=True, upload_to='static/main/img')
    image_8 = models.ImageField(verbose_name='Изображение', blank=True, upload_to='static/main/img')
    image_9 = models.ImageField(verbose_name='Изображение', blank=True, upload_to='static/main/img')