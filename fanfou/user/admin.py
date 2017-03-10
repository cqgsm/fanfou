from django.contrib import admin

from fanfou.common.generic import BMAdmin
from fanfou.user import User
from fanfou.user import UserForm


# Register your models here.

class UserAdmin(BMAdmin):
    list_display = ['username', 'name', 'nickname', 'age', 'birthday', 'created', 'creator',]
    fields = (('username',), ('password',), ('password2',), 
              ('nickname',), ('name',), ('age',), ('sex','gender'), ('birthday',),
              ('id_card'),
              ('mobile_phone',), ('landline',), ('used_email',), ('qq','wx',),  
              ('sina_weibo','alipay',), ('nationality','province','city','county',), ('address'),
              )
    form = UserForm

admin.site.register(User, UserAdmin)