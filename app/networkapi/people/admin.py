from django.contrib import admin
from adminsortable.admin import SortableAdmin

from networkapi.people.models import (
    Person,
    InternetHealthIssue,
    Affiliation,
)
from networkapi.people.forms import PersonAdminForm


class PersonAdmin(SortableAdmin):
    form = PersonAdminForm
    sortable_change_list_template = (
        'shared/adminsortable_change_list_custom.html'
    )

    class Media:
        js = ('/static/people/js/admin.js',)


admin.site.register(Person, PersonAdmin)
admin.site.register(InternetHealthIssue)
admin.site.register(Affiliation)
