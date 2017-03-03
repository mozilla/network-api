from django.db import models

class Person(models.Model):
    """
    A member of the Network
    """
    name = models.CharField(max_length=120)
    role = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    teams = models.ManyToManyField(Team)
    links = models.ManyToManyField(Link)
    image = models.CharField(max_length=4096)

    class Meta:
        verbose_name_plural = 'people'

    def __str__(self):
        return str(self.name)


class Team(models.Model):
    name = models.CharField(max_length=120)

class Link(models.Model):
    url = models.CharField(max_length=4096)
