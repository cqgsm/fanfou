'''
Created on 2016-9-18

@author: yimeng
'''
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

from ..models import User, Evaluation

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    
    default_error_messages = {
        'inactive_account': _('User account is disabled.'),
        'invalid_credentials': _('Unable to login with provided credentials.')
    }

    def __init__(self, *args, **kwargs):
        super(UserLoginSerializer, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self, attrs):
        self.user = authenticate(username=attrs.get("username"), password=attrs.get('password'))
        if self.user:
            if not self.user.is_active:
                raise serializers.ValidationError(self.error_messages['inactive_account'])
            return attrs
        else:
            raise serializers.ValidationError(self.error_messages['invalid_credentials'])


class TokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source='key')
    username = serializers.SerializerMethodField()
    class Meta:
        model = Token
        fields = ("auth_token",'username')

    def get_username(self, obj):
        return obj.user.username


class UserCreaterSerializer(serializers.ModelSerializer):
    mobile_phone = serializers.CharField(required=True, allow_null=False,
                                         validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(required=True, allow_null=False, min_length=6 )
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'mobile_phone')

class UserRetrieveUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'mobile_phone', 'nickname', 'name', 'sex', 'birthday', 'age', 'picture', 'credit',
                  'popularity')
        read_only_fields = ('username', 'credit', 'popularity')



class EvaluationListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = ('user', 'related_dating', 'impression', 'content', 'url')

class EvaluationRetrieveUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = ('user', 'related_dating', 'impression', 'content', 'url')
        read_only_fields = ('user', 'related_dating', 'url')
