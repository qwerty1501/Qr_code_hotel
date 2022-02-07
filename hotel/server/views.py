from django.shortcuts import redirect
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *
from rest_framework import generics, status
# from .permissions import *

from django.contrib.auth import get_user_model

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

from string import digits


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return redirect('menu')
        return super(LoginAPI, self).post(request, format=None)


class RoomUpdatePassword(APIView):

    def post(self, request):
        Room = get_user_model()
        room = Room.objects.get(room_number=int(request.data.get('room_number')))
        new_password = Room.objects.make_random_password(4, digits)
        # room.pin_code = new_password
        room.unhashed_password = new_password
        room.set_password(new_password)
        room.save()
        return Response(new_password)


class RoomCreateView(generics.CreateAPIView):
    serializer_class = RoomCreateSerializer
    permission_classes = (IsAdminUser, )


class RoomListView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (IsAdminUser, )


# class LoginAPIView(APIView):
#     permission_classes = [AllowAny]
#     serializer_class = LoginSerializer

    # def post(self, request):
    #     serializer = self.serializer_class(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #
    #     return Response(serializer.data, status=status.HTTP_200_OK)


class MenuCreateView(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def get_queryset(self):
    #     if self.request.method == 'POST':
    #         return OrderCreateSerializer
    #     else:
    #         return OrderSerializer


class OrdersView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAdminUser, )

