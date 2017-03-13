from django.conf.urls import include, url
from django.contrib import admin

api_urls = [
    # url(r'^$',include('doc.urls')),
    url(r'^user/',include('fanfou.apps.user.api.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_docs.urls')),
]

urlpatterns = [
    # Examples:
    # url(r'^$', 'fanfou.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/',include(api_urls)),
    url(r'^wechat/', include('fanfou.apps.wechat.urls',namespace='wechat')),
]
