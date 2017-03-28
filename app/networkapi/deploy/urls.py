from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from networkapi.deploy import views

urlpatterns = [
    url(r'^(?P<env>(STAGING|PROD))/$', views.deployView),
]

urlpatterns = format_suffix_patterns(urlpatterns)
