# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("authentication.urls")), # Auth routes - login / register
    path("", include("logcutting_loglist.urls")),             # UI Kits Html files
    path("", include("logcutting_sawnlog.urls")),           # UI Kits Html files
    path("", include("logcutting_supplier.urls")),
    path("", include("logcutting_partai.urls")),
    path("", include("rotary_bobin.urls")),
    path("", include("rotary_jeniscore.urls")),
    path("", include("rotary_mesinrotary.urls")),
    # path("", include("app.urls"))
]
