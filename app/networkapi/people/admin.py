from django.contrib import admin

from networkapi.people.models import (
    Person,
    InternetHealthIssue,
    Affiliation,
)
from networkapi.people.forms import PersonAdminForm


class AffiliationAdmin(admin.TabularInline):
    model = Affiliation
    extra = 1


class PersonAdmin(admin.ModelAdmin):
    form = PersonAdminForm
    inlines = [
        AffiliationAdmin,
    ]

    class Media:
        js = ('/static/people/js/admin.js',)


admin.site.register(Person, PersonAdmin)
admin.site.register(InternetHealthIssue)
