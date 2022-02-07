import random
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
import qrcode
from django.http import HttpResponse
from django.utils import timezone


from django.db import models

from .managers import CustomUserManager


class Category(models.Model):
    title = models.CharField('Категория', max_length=30)
    foods = models.ForeignKey('Menu', on_delete=models.CASCADE)


class Menu(models.Model):
    title = models.CharField('Название блюда', max_length=200)
    content = models.TextField('Описание блюда')
    weight = models.IntegerField('Вес блюда')
    image = models.ImageField(upload_to='dishes/')
    in_stock = models.BooleanField('В наличии', default=True)
    price = models.IntegerField('Цена', default=0)

    def __str__(self):
        return self.title


class Order(models.Model):
    new_order = models.ForeignKey('Room', on_delete=models.DO_NOTHING)
    order_date = models.DateTimeField('Время заказа', auto_now_add=True)
    is_done = models.BooleanField('Готово', default=False)
    foods = models.ManyToManyField(Menu)

    def __str__(self):
        return f'Заказ комнаты номер {self.new_order}'


class Room(AbstractBaseUser, PermissionsMixin):
    room_number = models.CharField('Номер комнаты', unique=True, blank=True, max_length=5)
    qrcode = models.ImageField(upload_to='qr_codes/', blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    unhashed_password = models.CharField(max_length=5)

    USERNAME_FIELD = 'room_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.room_number}'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        input_data = f"http://127.0.0.1:8000/room/{self.room_number}"

        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5)
        qr.add_data(input_data)
        qr.make(fit=True)
        self.qrcode = qr.make_image(fill='black', back_color='white')
        self.qrcode.save(f'media/qrcode{self.room_number}.png')
        self.qrcode = f'qrcode{self.room_number}.png'
        self.save_base(self.qrcode)
