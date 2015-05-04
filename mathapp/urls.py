# -*- coding: UTF-8 -*-

from django.conf.urls import patterns, url

import mathapp

urlpatterns = patterns('',
    # launch task
    url(r'^add/(?P<a>\d+)/(?P<b>\d+)/$', 'mathapp.views.add_delay'),
    url(r'^mul/(?P<a>\d+)/(?P<b>\d+)/$', 'mathapp.views.mul_delay'),
    url(r'^fac/(?P<n>\d+)/$', 'mathapp.views.fac_delay'),
        
    # view task
    url(r'^task/(?P<task_id>.*)/$', 'mathapp.views.task_result', name='task_result'),
)
