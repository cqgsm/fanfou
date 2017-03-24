
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view


from ..models import User, Evaluation
from .serializers import ( UserLoginSerializer, TokenSerializer, UserCreaterSerializer,
                           UserRetrieveUpdateSerializer, EvaluationListCreateSerializer,
                           EvaluationRetrieveUpdateSerializer)
from .permissions import EvaluationPermission

@api_view(('GET',))
def api_root(request, format=None):
    '''
    用户登录 API
    '''
    return Response({
        '用户注册': reverse('user-create', request=request, format=format),
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

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreaterSerializer

class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = UserRetrieveUpdateSerializer
    def get_object(self):
        user = get_object_or_404(User, auth_user=self.request.user)
        return user

class EvaluationListCreateAPIView(ListCreateAPIView):
    serializer_class = EvaluationListCreateSerializer
    def get_queryset(self):
        evaluation_set = Evaluation.objects.filter(user=self.request.user)
        return evaluation_set

class EvaluationRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = EvaluationRetrieveUpdateSerializer
    permission_classes = (EvaluationPermission,)
    queryset = Evaluation.objects.all()