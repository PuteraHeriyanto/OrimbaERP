
from django.contrib import admin

from .models import SawnLog
from import_export import resources
from import_export.admin import ImportMixin


class SawnLogResource(resources.ModelResource):
    class Meta:
        model = SawnLog
        fields = ['log_id', 'sawn_id', 'sawn_length', 'diameter_1', 'diameter_2','average_diameter','sawn_grade','volume']

@admin.register(SawnLog)
class SawnLogAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['log_id', 'sawn_id', 'sawn_length', 'diameter_1', 'diameter_2','average_diameter','sawn_grade','volume']
    resource_class = SawnLogResource
