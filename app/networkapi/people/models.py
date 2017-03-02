from django.db import models

class Person(models.Model):
    name: models.CharField(max_length=120)
    role: models.CharField(max_length=120)
    location: models.CharField(max_length=120)
    teams: models.ManyToManyField(Team)
    links: models.ManyToManyField(Link)
    image: models.CharField(max_length=4096)
    featured: models.BooleanField(default=False)
    

class Team(models.Model):
    name: models.CharField(max_length=120)

class Link(models.Model):
    url: models.CharField(max_length=4096)
