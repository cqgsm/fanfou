from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from .views import ( UserLoginAPIView, UserLogoutAPIView, UserCreateAPIView,
                     UserRetrieveUpdateAPIView, EvaluationListCreateAPIView,
                     EvaluationRetrieveUpdateAPIView, api_root )


urlpatterns = [
    url(r'^$',api_root,name="user-root"),
    url(r'^registered/$', UserCreateAPIView.as_view(), name="user-create"),
    url(r'^login/$', UserLoginAPIView.as_view(), name="login"),
    url(r'^logout/$', UserLogoutAPIView.as_view(), name="logout"),
    url(r'^detail/$', UserRetrieveUpdateAPIView.as_view(), name="user-detail"),
    url(r'^evaluation/$', EvaluationListCreateAPIView.as_view(), name="user-evaluation"),
    url(r'^evaluation/(?P<pk>[^/.]+)/$', EvaluationRetrieveUpdateAPIView.as_view(), name="evaluation-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)