from django.contrib import admin

from networkapi.features.models import Feature
from networkapi.features.forms import FeatureAdminForm


class FeatureAdmin(admin.ModelAdmin):
    form = FeatureAdminForm


admin.site.register(Feature, FeatureAdmin)
