from django.conf.urls import url

from networkapi.features.views import (
    FeatureListView,
    FeatureView,
)

urlpatterns = [
    url('^$', FeatureListView.as_view(), name='feature-list'),
    url(r'^(?P<pk>[0-9]+)/', FeatureView.as_view(), name='feature'),
]
