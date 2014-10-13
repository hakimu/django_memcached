from django.conf.urls import patterns, include, url
from django.contrib import admin

from django_memcached.views import today_is, show_album, show_artist

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_memcached.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/$', today_is),
    url(r'^records/$',show_album),
    url(r'^artist/$',show_artist),
)
