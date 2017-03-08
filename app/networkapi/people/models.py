from django.db import models
from datetime import datetime, timezone
from slugify import slugify
from adminsortable.models import SortableMixin
import os


def person_image_path(instance, filename):
    return 'images/people/{name}_{timestamp}{ext}'.format(
        name=slugify(instance.name, max_length=300),
        timestamp=str(
            int((
                datetime.now(tz=timezone.utc) -
                datetime(1970, 1, 1, tzinfo=timezone.utc)
            ).total_seconds())
        ),
        ext=os.path.splitext(filename)[1]
    )


class Team(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return str(self.name)


class Link(models.Model):
    url = models.CharField(max_length=4096)
    name = models.CharField(max_length=300)

    def __str__(self):
        return str(self.url)


class Person(SortableMixin):
    """
    A member of the Network
    """
    name = models.CharField(max_length=300)
    role = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    image = models.ImageField(
        max_length=2048,
        upload_to=person_image_path,
    )
    teams = models.ManyToManyField(
        Team,
        related_name='people',
    )
    links = models.ManyToManyField(
        Link,
        related_name='people',
    )
    order = models.PositiveIntegerField(
        default=0,
        editable=False,
        db_index=True,
    )

    class Meta:
        verbose_name_plural = 'people'
        ordering = ('order',)

    def __str__(self):
        return str(self.name)
