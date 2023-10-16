# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from logcutting_loglist import views

urlpatterns = [

    # The home page

    path('loglistnew', views.LogListDataCreateView.as_view(), name='new-LogListData'),
    # path('', views.index, name='home'),

    re_path(r'^loglist/(?:(?P<pk>[\w]+)/)?(?:(?P<action>[^\d]+)/)?', views.LogListView.as_view(),
            name='loglist'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
