'''
Created on 2017-3-2

@author: yimeng
'''
from datetime import datetime

from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from fanfou.common.utils import getPinyin
# Create your models here.

class BM(models.Model):
    creator = models.ForeignKey(User,blank=True, null=True, verbose_name=_('creator'), related_name="%(app_label)s_%(class)s_creator")
    created = models.DateTimeField(_('create time'),auto_now_add=True)
    updater = models.ForeignKey(User,blank=True, null=True, verbose_name=_('updater'), related_name="%(app_label)s_%(class)s_updater")
    updated = models.DateTimeField(_('update time'), auto_now=True)
    deleted = models.DateTimeField(_('delete time'), blank=True, null=True, default=None)
    pinyin = models.CharField(max_length=20, blank=True, null=True)
    in_use = models.NullBooleanField(_('in use'), default=True, blank=True, null=True)
    remark = models.TextField(_('remark'), blank=True, null=True)
    pinyin_field = None
    
    class Meta:
        abstract = True
        
    def save(self, *args, **kwargs):
        self.get_pinyin()
        super(BM, self).save(*args, **kwargs)
        
    
    def get_pinyin(self):
        if self.pinyin_field is None:
            return None
        else:
            pinyin_code = setattr(self, "pinyin", getPinyin(getattr(self, self.pinyin_field)))
            return pinyin_code
        
    def __str__(self):
        return self.name
        

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

class BMAdmin(ModelAdmin):
    exclude = ['creator', 'created', 'updater', 'updated', 'deleted', 'pinyin', 'remark', 'in_use',]
    actions_on_top = False
    actions_on_bottom = True
    def save_model(self, request, obj, form, change):
        if change:
            setattr(obj, 'updater', request.user)
            setattr(obj, 'updated', datetime.now())
        else:
            setattr(obj,'creator',request.user)
            setattr(obj,'created',datetime.now())
        super(BMAdmin, self).save_model(request, obj, form, change)
        
        
    