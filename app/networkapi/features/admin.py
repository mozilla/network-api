from django.contrib import admin
from adminsortable.admin import SortableAdmin

from networkapi.features.models import Feature
from networkapi.features.forms import FeatureAdminForm


class FeatureAdmin(SortableAdmin):
    form = FeatureAdminForm
    sortable_change_list_template = (
        'shared/adminsortable_change_list_custom.html'
    )

admin.site.register(Feature, FeatureAdmin)
