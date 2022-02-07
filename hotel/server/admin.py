from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import *
from .models import *
# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomRoomCreationForm
    form = CustomRoomChangeForm
    model = Room
    list_display = ('room_number', 'is_staff', 'is_active',)
    list_filter = ('room_number', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('room_number', 'password', 'unhashed_password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('room_number', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('room_number',)
    ordering = ('room_number',)


admin.site.register(Room, CustomUserAdmin)

admin.site.register(Order)
admin.site.register(Menu)
