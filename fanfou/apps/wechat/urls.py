from django.conf.urls import include, url
from fanfou.apps.wechat.views import wechat_main, get_access_token
urlpatterns = [
    url(r'^index/$',wechat_main),
    url(r'^access_token/$', get_access_token),
]
