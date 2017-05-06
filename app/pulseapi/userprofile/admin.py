"""
Admin setings for UserProfile app
"""
from django.contrib import admin
from .models import UserProfile


class UserBookmarkInline(admin.TabularInline):
    """
    We need an inline widget before we can do anything
    with the user/entry bookmark data.
    """
    model = UserProfile.bookmarks.through
    verbose_name = 'UserBookmark'


class UserProfileAdmin(admin.ModelAdmin):
    """
    Show a list of entries a user has submitted in the UserProfile Admin app
    """
    fields = ('user', 'bookmarks')
    readonly_fields = ('user','bookmarks')

    # this allows us to create/edit/delete/etc bookmarks:
    inlines = [ UserBookmarkInline ]

    def entries(self, instance):
        """
        Show all entries as a string of titles. In the future we should make them links.
        """
        return ", ".join([str(entry) for entry in instance.entries.all()])


admin.site.register(UserProfile, UserProfileAdmin)
