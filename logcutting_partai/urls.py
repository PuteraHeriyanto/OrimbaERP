# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from logcutting_partai import views

urlpatterns = [

    # The home page

    path('partainew', views.PartaiDataCreateView.as_view(), name='new-PartaiData'),
    # path('', views.index, name='home'),

    re_path(r'^partai/(?:(?P<pk>[\w-]+)/)?(?:(?P<action>[^\d]+)/)?', views.PartaiView.as_view(),
            name='partai'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
