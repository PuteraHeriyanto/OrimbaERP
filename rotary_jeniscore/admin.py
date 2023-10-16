
from django.contrib import admin

from .models import JenisCore
from import_export import resources
from import_export.admin import ImportMixin


class JenisCoreResource(resources.ModelResource):
    class Meta:
        model = JenisCore
        fields = ['id_jenis_core', 'faktor_koreksi']

@admin.register(JenisCore)
class JenisCoreAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['id_jenis_core', 'faktor_koreksi']
    resource_class = JenisCoreResource
