from string import digits
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, room_number, password=None, **extra_fields):
        if not room_number:
            raise ValueError('Должен быть указан номер комнаты.')
        room_number = room_number
        user = self.model(room_number=room_number, **extra_fields)
        if password is None:
            password = BaseUserManager().make_random_password(4, digits)
        user.unhashed_password = password

        print(f"Комната: {room_number}. Пин-код: {password}")
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, room_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        if password is None:
            password = BaseUserManager().make_random_password(4, digits)

            print(f"Комната: {room_number}. Пин-код: {password}")

        return self.create_user(room_number, password=password, **extra_fields)
