
from django.contrib import admin

from .models import Supplier
from import_export import resources
from import_export.admin import ImportMixin


class SupplierResource(resources.ModelResource):
    class Meta:
        model = Supplier
        fields = ['supplier_id', 'supplier_name']

@admin.register(Supplier)
class SupplierAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['supplier_id', 'supplier_name']
    resource_class = SupplierResource
