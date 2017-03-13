from django.contrib import admin
from adminsortable.admin import SortableAdmin

from networkapi.people.models import (
    Person,
    Link,
    InternetHealthIssue,
    Affiliation,
)
from networkapi.people.forms import PersonAdminForm


class PersonAdmin(SortableAdmin):
    form = PersonAdminForm
    sortable_change_list_template = (
        'people/adminsortable_change_list_custom.html'
    )

    class Media:
        js = ('/static/people/js/admin.js',)


admin.site.register(Person, PersonAdmin)
admin.site.register(Link)
admin.site.register(InternetHealthIssue)
admin.site.register(Affiliation)
