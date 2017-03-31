from django.contrib import admin
from mezzanine.pages.admin import PageAdmin

from networkapi.landingpage.models import (
    LandingPage,
    Signup,
    FooterLink,
)


class LandingPageAdmin(PageAdmin):
    fieldsets = (
        (None, {
            'fields': [
                'title',
                'label',
                'featured',
                'header',
                'content',
                'signup',
            ]
        }),
        ('Publishing', {
            'fields': [
                'status',
                ("publish_date", "expiry_date"),

            ]
        }),
    )


admin.site.register(LandingPage, LandingPageAdmin)
admin.site.register(Signup)
admin.site.register(FooterLink)
