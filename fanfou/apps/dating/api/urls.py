from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from fanfou.apps.dating.api.views import ( DatingListCreateAPIView, DatingRetrieveUpdateAPIView, ParticipantCreateAPIView,
                                           ParticipantRetrieveUpdateDestroyAPIView,test )

urlpatterns = [
    url(r'^$', DatingListCreateAPIView.as_view(), name="dating-create"),
    url(r'^(?P<pk>[0-9]+)/$', DatingRetrieveUpdateAPIView.as_view(), name="dating-detail"),
    url(r'^participant/$', ParticipantCreateAPIView.as_view(), name="participant-create"),
    url(r'^participant/(?P<pk>[^/.]+)/$', ParticipantRetrieveUpdateDestroyAPIView.as_view(), name="participant-delete"),
    url(r'^test/$', test),
]

urlpatterns = format_suffix_patterns(urlpatterns)