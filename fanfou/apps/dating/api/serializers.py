from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from fanfou.apps.dating.models import Dating, Participant


class ParticipantCreateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ('dating', 'agree', 'creator', 'created', 'pk')
        read_only_fields = ('creator','created', 'pk')

class ParticipantRetrieveUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ('agree',)

class DatingListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dating
        fields = ('title', 'description', 'location', 'dating_time', 'pay_method', 'pictures', 'status', 'creator',
                  'pk', 'url')
        read_only_fields = ('status', 'creator', 'url')

class DatingRetrieveUpdateSerializer(serializers.ModelSerializer):
    participant = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Dating
        fields = ('title', 'description', 'location', 'dating_time', 'pay_method', 'pictures', 'status', 'creator',
                  'participant', 'pk')
        read_only_fields = ('location', 'dating_time', 'pay_method', 'status', 'creator', 'pk')

    def get_participant(self, obj):
        '''
        得到对应约会申请人的列表
        :param obj:
        :return:
        '''
        participant_set = Participant.objects.filter(dating=obj)
        participant = ParticipantCreateListSerializer(participant_set, many=True).data
        return participant