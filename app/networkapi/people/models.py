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


def person_partnership_logo_path(instance, filename):
    return 'images/people/{name}_partnership_{timestamp}{ext}'.format(
        name=slugify(instance.name, max_length=300),
        timestamp=str(
            int((
                datetime.now(tz=timezone.utc) -
                datetime(1970, 1, 1, tzinfo=timezone.utc)
            ).total_seconds())
        ),
        ext=os.path.splitext(filename)[1]
    )


class Link(models.Model):
    url = models.CharField(max_length=4096)
    name = models.CharField(max_length=300)

    def __str__(self):
        return str(self.url)


class InternetHealthIssue(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class Affiliation(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return str(self.name)


class Person(SortableMixin):
    """
    A member of the Network
    """
    name = models.CharField(max_length=300)
    role = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    quote = models.TextField(
        max_length=1000,
        null=True,
        blank=True,
    )
    bio = models.TextField(
        max_length=5000,
        default='',
    )
    image = models.ImageField(
        max_length=2048,
        upload_to=person_image_path,
        default='images/shared/default.png',
    )
    partnership_logo = models.ImageField(
        max_length=2048,
        upload_to=person_partnership_logo_path,
        default='images/shared/default.png',
    )
    affiliations = models.ManyToManyField(
        Affiliation,
        related_name='people',
    )
    links = models.ManyToManyField(
        Link,
        related_name='people',
        blank=True,
    )
    internet_health_issues = models.ManyToManyField(
        InternetHealthIssue,
        related_name='people'
    )
    order = models.PositiveIntegerField(
        default=0,
        editable=False,
        db_index=True,
    )
    featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'people'
        ordering = ('order',)

    def __str__(self):
        return str(self.name)
