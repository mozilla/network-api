from django.utils import timezone
from django.db import models

from django.db import models

from networkapi.utility.images import get_image_upload_path


def get_features_image_upload_path(instance, filename):
    return get_image_upload_path(
        app_name='features',
        prop_name='name',
        instance=instance,
        current_filename=filename
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
        help_text='Publish this feature after this date and time (UTC)', 
        default=timezone.now,
        null=True,
    )
    expires = models.DateTimeField(
        help_text='Unpublish this feature after this date and time (UTC). '
                  'Leave blank to never unpublish',
        default=None,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name_plural = 'features'

    def __str__(self):
        return str(self.name)
