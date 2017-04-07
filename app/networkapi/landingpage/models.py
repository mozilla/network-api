from django.db import models
from mezzanine.pages.models import Page
from mezzanine.core.fields import RichTextField


class Signup(models.Model):
    header = models.CharField(max_length=500)
    description = RichTextField("description")

    def __str__(self):
        return str(self.header)


class LandingPage(Page):
    LABELS = (
        ('read', 'Read and contribute'),
        ('write', 'Create and inspire'),
    )

    label = models.CharField(
        max_length=12,
        choices=LABELS,
        default='read',
    )

    # featured-image = s3boto3 stuffs

    featured = models.BooleanField(default=False)

    header = models.CharField(max_length=500)
    content = RichTextField("Main body content")

    signup = models.ForeignKey(
        Signup,
        related_name='page',
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return str(self.title)
