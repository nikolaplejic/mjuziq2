from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'mjuziqmgr.views.index', name='index'),
    url(r'^albums/', include('mjuziqmgr.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
