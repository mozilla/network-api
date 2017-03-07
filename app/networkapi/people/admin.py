from django.contrib import admin

from networkapi.people.models import Person, Link, Team

admin.site.register(Person)
admin.site.register(Link)
admin.site.register(Team)