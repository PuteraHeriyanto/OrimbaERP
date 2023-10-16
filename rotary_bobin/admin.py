
from django.contrib import admin

from .models import Bobin
from import_export import resources
from import_export.admin import ImportMixin


class BobinResource(resources.ModelResource):
    class Meta:
        model = Bobin
        fields = ['id_bobin', 'nama_bobin']

@admin.register(Bobin)
class BobinAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['id_bobin', 'nama_bobin']
    resource_class = BobinResource
