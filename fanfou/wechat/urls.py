from django.conf.urls import include, url
from wechat.views import weixin_main
urlpatterns = [
    url(r'^index/$',weixin_main),
]