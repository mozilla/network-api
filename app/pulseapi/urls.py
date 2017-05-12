from django.conf.urls import url, include

urlpatterns = [
    url(r'^entries/',  include('pulseapi.entries.urls')),
    url(r'^tags/',     include('pulseapi.tags.urls')),
    url(r'^issues/',   include('pulseapi.issues.urls')),
    url(r'^creators/', include('pulseapi.creators.urls')),
    url(r'^',         include('pulseapi.utility.urls')),
]
