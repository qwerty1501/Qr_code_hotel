from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from knox.views import LoginView

from .views import *
from knox import views as knox_views


urlpatterns = [
    path('room/menu', OrderCreateView.as_view(), name='menu'),
    path('room/', RoomListView.as_view()),
    path('room/create/', RoomCreateView.as_view()),
    path('room/update-password/', RoomUpdatePassword.as_view()),
    path('room/login/', LoginAPI.as_view()),
    path('logout/', knox_views.LogoutView.as_view()),
    path('logoutall/', knox_views.LogoutAllView.as_view()),
    path('orders/', OrdersView.as_view())
    # path('auth_login/', LoginView.as_view())
    ]
