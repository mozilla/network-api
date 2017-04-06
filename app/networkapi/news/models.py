from django.utils import timezone
from django.db import models
from django.db.models import Q

from networkapi.utility.images import get_image_upload_path


def get_news_glyph_upload_path(instance, filename):
    return get_image_upload_path(
        app_name='news',
        prop_name='headline',
        instance=instance,
        current_filename=filename
    )


class NewsQuerySet(models.query.QuerySet):
    """
    A QuerySet for news that filters for published records
    """
    def published(self):
        now = timezone.now()
        return self.filter(
            Q(expires__gt=now) | Q(expires__isnull=True),
            publish_after__lt=now,
        )


class News(models.Model):
    """
    Medium blog posts, articles and other media
    """
    headline = models.CharField(
        max_length=300,
        help_text='Title of the article, post or media clip',
    )
    outlet = models.CharField(
        max_length=300,
        help_text='Source of the article or media clip',
    )
    date = models.DateField(
        help_text='Publish date of the media',
    )
    link = models.URLField(
        max_length=500,
        help_text='URL link to the article/media clip',
    )
    excerpt = models.TextField(
        max_length=1000,
        help_text='A small extract from the article',
        blank=True,
        null=True,
    )
    author = models.CharField(
        max_length=300,
        help_text='Name of the author of this news clip',
        blank=True,
        null=True,
    )
    glyph = models.FileField(
        max_length=2048,
        help_text='Image associated with the article',
        upload_to=get_news_glyph_upload_path,
        null=True,
        blank=True,
    )
    featured = models.BooleanField(
        help_text='Do you want to feature this news piece?',
        default=False,
    )
    publish_after = models.DateTimeField(
        help_text='Make this news visible only '
                  'after this date and time (UTC)',
        null=True,
    )
    expires = models.DateTimeField(
        help_text='Hide this news after this date and time (UTC)',
        default=None,
        null=True,
        blank=True
    )

    objects = NewsQuerySet.as_manager()

    class Meta:
        verbose_name_plural = 'news'
        ordering = ('-date',)

    def __str__(self):
        return str(self.headline)
