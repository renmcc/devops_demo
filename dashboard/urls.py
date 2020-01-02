#!/usr/bin/env python
#coding:utf-8
#__time__: 2019/12/28 20:24
#__author__ = 'ren_mcc'

from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^indext/', views.index_template),
    url(r'^articles/([0-9]{4})/$', views.articles),
    url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]+/$)', views.articles),
    #url(r'^hellot',views.MyView.as_view()),
    url(r'^hellot/',views.UserListView.as_view(), name='hellot'),
    url(r'^hellot2/',views.UsersView.as_view(), name='hellot2')
]
