from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return str(self.name)


class Link(models.Model):
    url = models.CharField(max_length=4096)
    name = models.CharField(max_length=300)

    def __str__(self):
        return str(self.url)


class Person(models.Model):
    """
    A member of the Network
    """
    name = models.CharField(max_length=300)
    role = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    image = models.ImageField(
        max_length=2048,
        upload_to='images/people',
    )
    teams = models.ManyToManyField(
        Team,
        related_name='people',
    )
    links = models.ManyToManyField(
        Link,
        related_name='people',
    )

    class Meta:
        verbose_name_plural = 'people'

    def __str__(self):
        return str(self.name)
