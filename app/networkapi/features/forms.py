from django import forms
from django.utils import timezone
from django.contrib.admin.widgets import AdminSplitDateTime

from networkapi.features.models import Feature


class FeatureAdminForm(forms.ModelForm):
    publish_after = forms.SplitDateTimeField(
        widget=AdminSplitDateTime,
        initial=lambda: timezone.now(),
        help_text='Publish date of the media',
    )

    class Meta:
        model = Feature
        fields = (
            'name',
            'description',
            'link_label',
            'link_url',
            'image',
            'featured',
            'publish_after',
            'expires',
        )
