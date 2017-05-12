import factory
from faker import Factory as FakerFactory
from django.contrib.auth import get_user_model
from pulseapi.entries.models import Entry


faker = FakerFactory.create()


class EntryFactory(factory.DjangoModelFactory):

    title = factory.LazyAttribute(
        lambda o: 'title '+' '.join(faker.words(nb=1))
    )
    description = factory.LazyAttribute(
        lambda o: 'description '+''.join(faker.sentence(nb_words=20))
    )
    content_url = 'http://example.org/image.png'
    featured = False
    published_by = factory.LazyAttribute(
        lambda o: get_user_model().objects.all()[0]
    )
    is_approved = True

    class Meta:
        model = Entry
