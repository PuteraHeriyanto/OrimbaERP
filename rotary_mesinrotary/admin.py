
from django.contrib import admin

from .models import MesinRotary
from import_export import resources
from import_export.admin import ImportMixin


class MesinRotaryResource(resources.ModelResource):
    class Meta:
        model = MesinRotary
        fields = ['id_mesin_rotary', 'mesin_rotary']

@admin.register(MesinRotary)
class MesinRotaryAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['id_mesin_rotary', 'mesin_rotary']
    resource_class = MesinRotaryResource
