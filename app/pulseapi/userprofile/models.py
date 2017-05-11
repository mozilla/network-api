from django.db import models
from django.conf import settings

class UserProfile(models.Model):
    """
    This is the network-pulse-specific user profile,
    which is used to track entry bookmarks for individual
    users.

    User profiles are tied to Django users, such that
    when a django user is deleted, their associated
    profile, if there is one, is deleted as well.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_profile'
    )

    # "user X bookmarked entry Y" is a many to many relation,
    # for which we also want to know *when* a user bookmarked
    # a specific entry. As such, we use a helper class that
    # tracks this relation as well as the time it's created.
    bookmarks = models.ManyToManyField(
        'entries.Entry',
        through='UserBookmark',
        related_name='bookmark_by'
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "User profile"

class UserBookmark(models.Model):
    """
    This class is used to link users and entries through a
    "bookmark" relation. One user can bookmark many entries,
    and one entry can have bookmarks from many users.
    """
    entry = models.ForeignKey(
        'entries.Entry',
        on_delete=models.CASCADE,
        related_name='bookmarked_by'
    )

    profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='bookmark_entries'
    )

    timestamp = models.DateTimeField(
        auto_now=True,
    )
