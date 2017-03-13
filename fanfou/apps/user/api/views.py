# from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import login, logout ,authenticate
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from fanfou.apps.user.api.serializers import UserLoginSerializer, TokenSerializer
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view


@api_view(('GET',))
def api_root(request, format=None):
    '''
    用户登录 API
    '''
    return Response({
        # '用户创建': reverse('create', request=request, format=format),
        '用户登录': reverse('login', request=request, format=format),
        '用户注销': reverse('logout', request=request, format=format)
    })

class UserLoginAPIView(GenericAPIView):
    '''
    用户登录，获取 token
    '''
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserLoginSerializer
    def post(self, request, *args, **kwargs):
        # print(request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.user
            token, _ = Token.objects.get_or_create(user=user)
            return Response(
                data=TokenSerializer(token).data,
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

class UserLogoutAPIView(APIView):
    def post(self, request, *args, **kwargs):
        Token.objects.filter(user=request.user).delete()
        return Response(status=status.HTTP_200_OK)


# class UserCreateAPIView(GenericAPIView):
#     authentication_classes = ()
#     permission_classes = ()
#     serializer_class = UserSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             username = request.data.get('username')
#             email = request.data.get('email')
#             # 防止email重复
#             try:
#                 User.objects.get(email=email)
#             except ObjectDoesNotExist:
#                 pass
#             except MultipleObjectsReturned:
#                 return Response(data={'errors': 'Repeat email'}, status=status.HTTP_400_BAD_REQUEST)
#             else:
#                 return Response(data={'errors': 'Repeat email'}, status=status.HTTP_400_BAD_REQUEST)
#             password = request.data.get('password')
#             try:
#                 user = User.objects.create_user(username, email, password)
#             except IntegrityError:
#                 return Response(data={'errors': 'Repeat users'}, status=status.HTTP_400_BAD_REQUEST)
#             return Response(
#                 data=UserSerializer(user).data,
#                 status=status.HTTP_201_CREATED
#             )
#         else:
#             return Response(
#                 data=serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST,
#             )




# from django.contrib.auth.models import User, Group
# from rest_framework import viewsets
# from fanfou.apps.user.api.serializers import UserSerializer, GroupSerializer
#
#
# class UserViewSet(viewsets.ModelViewSet):
#     """
#     查看、编辑用户的界面
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#
#
# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     查看、编辑组的界面
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
