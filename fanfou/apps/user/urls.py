from django.conf.urls import url

from fanfou.apps.user import views
# template_name = {'template_name': 'rest_framework/login.html'}
redirect_url = '/api/user'
urlpatterns = [
    url(r'^login/$', views.api_login, {'redirect_url':redirect_url},name='login'),
    url(r'^logout/$', views.api_logout, {'redirect_url':redirect_url},name='logout'),
]
