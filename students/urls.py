from django.conf.urls import patterns, url

from students import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<student_id>\d+)/$', views.detail, name='detail'),
    url(r'^groups/$', views.groups, name='groups'),
    url(r'^group/(?P<group_id>\d+)/$', views.group_detail, name='group_detail'),

)