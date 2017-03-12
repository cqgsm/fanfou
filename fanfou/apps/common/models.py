from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from fanfou.common.utils import getPinyin


# Create your models here.

class CommonModel(models.Model):
    creator = models.ForeignKey(User,blank=True, null=True, verbose_name=_('creator'), related_name="%(app_label)s_%(class)s_creator")
    created = models.DateTimeField(_('create time'),auto_now_add=True)
    updater = models.ForeignKey(User,blank=True, null=True, verbose_name=_('updater'), related_name="%(app_label)s_%(class)s_updater")
    updated = models.DateTimeField(_('update time'), auto_now=True)
    deleted = models.DateTimeField(_('delete time'), blank=True, null=True, default=None)
    pinyin = models.CharField(max_length=20, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    
    pinyin_field = None
    
    class Meta:
        abstract = True
        
    def save(self, *args, **kwargs):
        self.get_pinyin()
        super(CommonModel,self).save(*args, **kwargs)
        
    
    def get_pinyin(self):
        if self.pinyin_field is None:
            return None
        else:
            pinyin_code = setattr(self, "pinyin", getPinyin(getattr(self, self.pinyin_field)))
            return pinyin_code
        

class ContactInfo(models.Model):
    mobile_phone = models.CharField(max_length=11, unique=True, blank=True, null=True)
    landline = models.CharField(_('landline'),max_length=20,blank=True,null=True)
    used_email = models.EmailField(blank=True,null=True)
    fax = models.CharField(_('fax'),max_length=30,blank=True,null=True)
    qq = models.CharField(max_length=13, unique=True, blank=True, null=True)
    wx = models.CharField(max_length=20, unique=True, blank=True, null=True)
    sina_weibo = models.CharField(max_length=256, blank=True, null=True)
    alipay = models.CharField(max_length=256, unique=True, blank=True, null=True)
    
    nationality = models.CharField(max_length=30, blank=True, null=True)
    province = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    county = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=220, blank=True, null=True)
    
    class Meta:
        abstract = True
        
    