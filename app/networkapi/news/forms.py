from django import forms
from django.forms.widgets import SelectDateWidget
from datetime import date

from networkapi.news.models import News


class NewsAdminForm(forms.ModelForm):
    date = forms.DateField(
        widget=SelectDateWidget(
            years=range(date.today().year + 3, date.today().year - 8, -1),
        ),
        initial=date.today(),
        help_text='Publish date of the media',
    )

    class Meta:
        model = News
        fields = (
            'headline',
            'outlet',
            'date',
            'link',
            'excerpt',
            'author',
            'glyph',
            'featured',
        )
