from django.contrib import admin
from adminsortable.admin import SortableAdmin

from networkapi.highlights.models import Highlight
from networkapi.highlights.forms import HighlightAdminForm


class HighlightAdmin(SortableAdmin):
    form = HighlightAdminForm

admin.site.register(Highlight, HighlightAdmin)
