# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

from logcutting_partai.models import Partai
from import_export import resources
from import_export.admin import ImportMixin


class PartaiResource(resources.ModelResource):
    class Meta:
        model = Partai
        fields = ['partai_id', 'supplier_id', 'date_arrived', 'log_cost']


@admin.register(Partai)
class PartaiAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['partai_id', 'supplier_id', 'date_arrived', 'log_cost']
    resource_class = PartaiResource
