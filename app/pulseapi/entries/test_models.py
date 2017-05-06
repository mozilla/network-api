import factory
from faker import Factory as FakerFactory

from pulseapi.entries.models import Entry
from pulseapi.userprofile.test_models import UserProfileFactory


faker = FakerFactory.create()


class EntryFactory(factory.DjangoModelFactory):

    title = factory.LazyAttribute(lambda o: 'title '+' '.join(faker.words(nb=1)))
    description = factory.LazyAttribute(lambda o: 'description '+''.join(faker.sentence(nb_words=20)))
    content_url = 'http://example.org/image.png'
    featured = False
    published_by_id = 1
    is_approved = True

    class Meta:
        model = Entry
