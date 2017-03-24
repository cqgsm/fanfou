from django.contrib.auth.models import User as Auth_User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from fanfou.apps.common.generic import BM, ContactInfo
from fanfou.apps.dating.models import Dating

class User(BM, ContactInfo, Auth_User):
    '''
    user table
    '''
    SEX_CHOICES = (
        ('0','Female'),
        ('1','male'),
        ('2','Not determined'),
    )
    auth_user = models.OneToOneField(Auth_User, parent_link=True)
    picture = models.CharField(max_length=260, blank=True, null=True)
    nickname = models.CharField(_('nickname'), max_length=60,blank=True,null=True)
    name = models.CharField(_('name'), max_length=60, blank=True, null=True)
    
    age = models.IntegerField(_('age'), blank=True, null=True)
    sex = models.CharField(_('sex'), max_length=1, choices=SEX_CHOICES, blank=True, null=True)
    gender = models.CharField(_('gender'), max_length=1, choices=SEX_CHOICES, blank=True, null=True)
    birthday = models.DateField(_('birthday'), blank=True, null=True)
    id_card = models.CharField(_('id_card'), max_length=20, blank=True, null=True)

    credit = models.IntegerField(blank=True, null=True)
    popularity = models.IntegerField(blank=True, null=True)

    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = 'user'

class Evaluation(BM):
    user = models.ForeignKey(Auth_User)
    related_dating = models.ForeignKey(Dating, blank=True, null=True)
    impression = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    content = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = _('Evaluation')
        verbose_name_plural = _('Evaluation')

    def __str__(self):
        return self.user.username