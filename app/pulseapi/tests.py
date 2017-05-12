import json

from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from pulseapi.entries.models import Entry
from pulseapi.entries.test_models import EntryFactory

from networkapi.utility.userpermissions import (
    is_staff_address,
    assign_group_policy,
    add_user_to_main_site,
)


def setup_groups():
    staff, created = Group.objects.get_or_create(name='staff')
    content_type = ContentType.objects.get_for_model(Entry)

    permission = Permission.objects.create(
        codename='can_add_entry',
        name='Can Add Entries',
        content_type=content_type
    )
    staff.permissions.add(permission)
    staff.save()

    permission = Permission.objects.create(
        codename='can_change_entry',
        name='Can Change Entries',
        content_type=content_type
    )
    staff.permissions.add(permission)
    staff.save()

    permission = Permission.objects.create(
        codename='can_delete_entry',
        name='Can Delete Entries',
        content_type=content_type
    )
    staff.permissions.add(permission)
    staff.save()


def setup_entries(test):
    if Entry.objects.all().count() > 0:
        return

    test.entries = [EntryFactory() for i in range(2)]
    for entry in test.entries:
        entry.save()


def create_logged_in_user(test, name, email, password="password1234"):
    test.username = name

    # create use instance
    User = get_user_model()
    user = User.objects.create(username=name, email=email, password=password)
    user.save()

    # make sure this user is in the staff group, too
    if is_staff_address(email):
        assign_group_policy(user, "staff")
        add_user_to_main_site(user)

    # verify the user was saved
    users = User.objects.filter(username=name)
    test.assertEqual(len(users) == 1, True)

    # log this user in for further testing purposes
    test.client = Client()
    test.client.force_login(user)


def generate_default_payload(values):
    return {
        'title': 'default title',
        'nonce': values['nonce'],
        'csrfmiddlewaretoken': values['csrf_token'],
        'content_url': 'http://example.com/',
        'tags': ['tag1', 'tag2']
    }


def generate_payload(test, data={}, payload=False):
    values = json.loads(str(test.client.get('/nonce/').content, 'utf-8'))

    if payload is False:
        payload = generate_default_payload(values)

    for key in data:
        payload[key] = data[key]

    return payload


class PulseMemberTestCase(TestCase):
    """
    A test case wrapper for "plain users" without any staff or admin rights
    """
    def setUp(self):
        setup_groups()
        create_logged_in_user(
            self,
            name="plain user",
            email="test@example.org"
        )
        setup_entries(self)

    def generatePostPayload(self, data={}):
        return generate_payload(self, data)


class PulseStaffTestCase(TestCase):
    """
    A test case wrapper for "staff" users, due to having a mozilla login
    """
    def setUp(self):
        setup_groups()
        create_logged_in_user(
            self,
            name="staff user",
            email="test@mozilla.org"
        )
        setup_entries(self)

    def generatePostPayload(self, data={}):
        return generate_payload(self, data)
