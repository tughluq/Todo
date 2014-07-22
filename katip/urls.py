# -*-coding: utf-8 -*-

'''
Created on 2014年7月18日

@author: ABDULLA
'''

from django.conf.urls import patterns, url

from katip import views

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns(
    '',
    url(r'^$', views.todolist, name='todo'),
    #url(r'^addtodo/$', views.addTodo, name='add'),
)


