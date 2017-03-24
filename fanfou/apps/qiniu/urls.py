from django.conf.urls import url
from .views import get_uptoken, get_downtoken
urlpatterns = [
    url(r'^uptoken/$', get_uptoken, name='uptoken'),
    url(r'^downtoken/$', get_downtoken, name='downtoken'),
]