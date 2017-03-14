from django.db import models
from datetime import datetime, timezone
from slugify import slugify
from adminsortable.models import SortableMixin
import os


def opportunity_image_path(instance, filename):
    return 'images/opportunity/{name}_{timestamp}{ext}'.format(
        name=slugify(instance.name, max_length=300),
        timestamp=str(
            int((
                datetime.now(tz=timezone.utc) -
                datetime(1970, 1, 1, tzinfo=timezone.utc)
            ).total_seconds())
        ),
        ext=os.path.splitext(filename)[1]
    )


class Opportunity(SortableMixin):
    name = models.CharField(max_length=300)
    header = models.TextField(max_length=5000)
    description = models.TextField(max_length=5000)
    link_text = models.CharField(max_length=300)
    link_url = models.URLField(max_length=2048)
    image = models.FileField(
        max_length=2048,
        upload_to=opportunity_image_path,
    )
    order = models.PositiveIntegerField(
        default=0,
        editable=False,
        db_index=True,
    )

    class Meta:
        verbose_name_plural = 'opportunities'
        ordering = ('order',)

    def __str__(self):
        return str(self.name)
