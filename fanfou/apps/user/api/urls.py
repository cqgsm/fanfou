from django.conf.urls import url
from fanfou.apps.user.api.views import UserLoginAPIView, UserLogoutAPIView,api_root
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$',api_root,name="user-root"),
    url(r'^login/$', UserLoginAPIView.as_view(), name="login"),
    url(r'^logout/$', UserLogoutAPIView.as_view(), name="logout"),
]

urlpatterns = format_suffix_patterns(urlpatterns)