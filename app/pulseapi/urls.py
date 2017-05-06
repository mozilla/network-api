from django.conf.urls import url, include
from .utility.posthelpers import nonce, userstatus

urlpatterns = [
    url(r'^entries/', include('pulseapi.entries.urls')),
    url(r'^tags/', include('pulseapi.tags.urls')),
    url(r'^issues/', include('pulseapi.issues.urls')),
    url(r'^creators/', include('pulseapi.creators.urls')),

    url(r'^nonce', nonce, name="get a new nonce value"),
    url(r'^userstatus', userstatus, name="get current user information"),
]
