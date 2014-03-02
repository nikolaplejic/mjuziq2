from django.conf.urls import patterns, url

from mjuziqmgr import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^todo/', views.todo, name='todo'),
)