'''
Created on 2017-2-25

@author: yimeng
'''
from django.contrib.auth import authenticate
from django.contrib.auth.models import User as Auth_User
from django.forms import Form, ModelForm, CharField, PasswordInput, ValidationError
from django.utils.translation import ugettext_lazy as _

from fanfou.apps.user.models import User


class LoginForm(Form):
    username = CharField(label="username", max_length=30)
    password = CharField(label="password", max_length=30, widget=PasswordInput)
    
    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username = username, password=password)
        if user is not None:
            if not user.is_active:
                raise ValidationError(_('The user is not available'))
        else:
            raise ValidationError(_('The account name or password is incorrect'))        
        
        
class UserForm(ModelForm):
    password2 = CharField(max_length=36, widget=PasswordInput, required=True)
    password = CharField(max_length=36, widget=PasswordInput, required=True)
    class Meta:
        model = User
        fields = '__all__'
    
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            Auth_User.objects.get(username=username)
            raise ValidationError(_('username is existd'))
        except Auth_User.DoesNotExist:
            return username
    
    def clean(self):
        try:
            password = self.cleaned_data['password']
            password2 = self.cleaned_data['password2']
            if password != password2:
                raise ValidationError('Two passwords are different')
        except KeyError:
            ValidationError('Two passwords are different')
        
            
            