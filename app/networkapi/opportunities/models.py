from django.db import models

from networkapi.utility.images import get_image_upload_path


def get_opportunities_image_upload_path(instance, filename):
    return get_image_upload_path(
        app_name='opportunities',
        prop_name='name',
        instance=instance,
        current_filename=filename
    )


class Opportunity(models.Model):
    name = models.CharField(
        max_length=300,
        help_text='Title of the opportunity',
    )
    description = models.TextField(
        max_length=5000,
        help_text='Description of the opportunity',
    )
    link_label = models.CharField(
        max_length=300,
        help_text='Text to show that links to this opportunity\'s '
                  'details page',
    )
    link_url = models.URLField(
        max_length=2048,
        help_text='Link to this opportunity\'s details page',
    )
    image = models.FileField(
        max_length=2048,
        help_text='Image representing this opportunity',
        upload_to=get_opportunities_image_upload_path,
    )
    featured = models.BooleanField(
        help_text='Do you want to feature this opportunity?',
        default=False,
    )

    class Meta:
        verbose_name_plural = 'opportunities'

    def __str__(self):
        return str(self.name)
