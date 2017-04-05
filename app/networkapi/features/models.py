from django.utils import timezone
from django.db import models
from django.db.models import Q

from networkapi.utility.images import get_image_upload_path


def get_features_image_upload_path(instance, filename):
    return get_image_upload_path(
        app_name='features',
        prop_name='name',
        instance=instance,
        current_filename=filename
    )


class FeatureQuerySet(models.query.QuerySet):
    """
    A QuerySet for features that filters for published features.
    """
    def published(self):
        now = timezone.now()
        return self.filter(
            Q(expires__gt=now) | Q(expires__isnull=True),
            publish_after__lt=now,
        )


class Feature(models.Model):
    name = models.CharField(
        max_length=300,
        help_text='Title of the feature',
    )
    description = models.TextField(
        max_length=5000,
        help_text='Description of the feature',
    )
    link_label = models.CharField(
        max_length=300,
        help_text='Text to show that links to this feature\'s '
                  'details page',
    )
    link_url = models.URLField(
        max_length=2048,
        help_text='Link to this feature\'s details page',
    )
    image = models.FileField(
        max_length=2048,
        help_text='Image representing this feature',
        upload_to=get_features_image_upload_path,
    )
    featured = models.BooleanField(
        help_text='Do you want to feature this feature?',
        default=False,
    )
    publish_after = models.DateTimeField(
        help_text='Make this feature visible only '
                  'after this date and time (UTC)'
                  'and time (UTC)',
        null=True,
    )
    expires = models.DateTimeField(
        help_text='Hide this feature after this date and time (UTC)',
        default=None,
        null=True,
        blank=True,
    )

    objects = FeatureQuerySet.as_manager()

    class Meta:
        verbose_name_plural = 'features'

    def __str__(self):
        return str(self.name)
