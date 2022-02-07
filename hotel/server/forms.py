from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Room


class CustomRoomCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Room
        fields = ('room_number',)


class CustomRoomChangeForm(UserChangeForm):

    class Meta:
        model = Room
        fields = ('room_number',)
