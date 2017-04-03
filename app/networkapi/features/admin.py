from django.contrib import admin
from adminsortable.admin import SortableAdmin

from networkapi.features.models import Feature


class FeatureAdmin(SortableAdmin):
    sortable_change_list_template = (
        'shared/adminsortable_change_list_custom.html'
    )

admin.site.register(Feature, FeatureAdmin)
