import json


from .models import UserProfile
from django.contrib.auth import get_user_model
from pulseapi.tests import PulseStaffTestCase, PulseMemberTestCase


class TestUserProfile(PulseStaffTestCase):

    def test_profile_creation(self):
        # get our user instance
        users = get_user_model().objects.filter(username=self.username)
        user = users[0]

        # verify that this user has an associated user profile
        found = UserProfile.objects.filter(user=user)
        has_profile = len(found) == 1
        self.assertEqual(has_profile, True)

        # verify there are zero bookmarks associated
        profile = found[0]
        bookmarks = profile.bookmarks.objects.all()
        self.assertEqual(len(bookmarks), 0)
