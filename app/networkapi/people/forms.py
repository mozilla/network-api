from django import forms
from django.core.exceptions import ValidationError
from django.forms.fields import Field

from networkapi.people.models import Person


class PersonAdminForm(forms.ModelForm):
    def clean_quote(self):
        cleaned_data = self.cleaned_data
        quote = cleaned_data.get('quote')

        if cleaned_data.get('featured') is True and not quote:
            raise ValidationError(
                Field.default_error_messages['required'],
                code='required',
            )
        return quote

    class Meta:
        model = Person
        fields = (
            'name',
            'role',
            'location',
            'bio',
            'image',
            'partnership_logo',
            'affiliations',
            'links',
            'internet_health_issues',
            'featured',
            'quote',
        )
