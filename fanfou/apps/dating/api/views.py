from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.pagination import PageNumberPagination

from fanfou.apps.common.api.permissions import UserIsCreator

from .serializers import ( DatingListCreateSerializer, DatingRetrieveUpdateSerializer,
                           ParticipantRetrieveUpdateSerializer, ParticipantCreateListSerializer,
                           Dating, Participant)
from .permissions import ParticipantPermission, DatingPermission


# Create your views here.

class DatingListCreateAPIView(ListCreateAPIView):
    '''
    创建约会
    '''
    queryset = Dating.objects.filter(status=0)
    serializer_class = DatingListCreateSerializer
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class DatingRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    '''
    约会详情和更新
    '''
    serializer_class = DatingRetrieveUpdateSerializer
    permission_classes = (DatingPermission, )
    queryset = Dating.objects.all()


class ParticipantCreateAPIView(CreateAPIView):
    '''申请人创建'''
    serializer_class = ParticipantCreateListSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class ParticipantRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    '''申请同意，删除'''
    serializer_class = ParticipantRetrieveUpdateSerializer
    permission_classes = (ParticipantPermission,)
    queryset = Participant.objects.all()

def test(request):
    from django.http import HttpResponse
    print(type(Participant.objects.all()))
    print(dir(Participant))
    return HttpResponse('')
