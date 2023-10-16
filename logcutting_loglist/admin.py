# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

from logcutting_loglist.models import LogList
from import_export import resources
from import_export.admin import ImportMixin


class LogListResource(resources.ModelResource):
    class Meta:
        model = LogList
        fields = ['log_id', 'partai_id', 'tanggal_kedatangan', 'supplier_id', 'grade']


@admin.register(LogList)
class LogListAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['log_id', 'partai_id', 'tanggal_kedatangan', 'supplier_id', 'grade']
    resource_class = LogListResource
