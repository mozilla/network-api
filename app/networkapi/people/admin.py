from django.contrib import admin
from adminsortable.admin import SortableAdmin

from networkapi.people.models import (
    Person,
    Link,
    Team,
    InternetHealthIssue,
    Affiliation,
)


class PersonAdmin(SortableAdmin):
    sortable_change_list_template = (
        'people/adminsortable_change_list_custom.html'
    )

admin.site.register(Person, PersonAdmin)
admin.site.register(Link)
admin.site.register(Team)
admin.site.register(InternetHealthIssue)
admin.site.register(Affiliation)