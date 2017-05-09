import json
from django.test import TestCase, Client
from django.contrib.auth import get_user_model


def setup_entries(test):
    test.entries = [EntryFactory() for i in range(2)]
    for entry in test.entries:
        entry.save()


def create_logged_in_user(test, username, email, password="password1234"):
    test.username = username

    # create use instance
    User = get_user_model();
    user = User.objects.create(username=username, email=email, password=password)
    user.save()

    # verify the user was saved
    users = User.objects.filter(username=username)
    test.assertEqual(len(users) == 1, True)

    # log this user in for further testing purposes
    test.client = Client()
    test.client.force_login(user);


def setup_data(test):
    # Set up with some curated data for all tests to use
    postresponse = test.client.post('/entries/', data=test.generatePostPayload())


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
        # setup_entries(self)
        user = create_logged_in_user(self, username="plain user", email="test@example.org")
        # setup_data(self)

    def generatePostPayload(self, data={}):
        return generate_payload(self, data)


class PulseStaffTestCase(TestCase):
    """
    A test case wrapper for "staff" users, due to having a mozilla login
    """
    def setUp(self):
        # setup_entries(self)
        user = create_logged_in_user(self, username="staff user", email="test@mozilla.org")
        # setup_data(self)

    def generatePostPayload(self, data={}):
        return generate_payload(self, data)