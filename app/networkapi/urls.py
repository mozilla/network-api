"""networkapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from mezzanine.core.views import direct_to_template
from mezzanine.conf import settings

admin.autodiscover()

urlpatterns = [
    url("^admin/", include(admin.site.urls)),
    url(r'^rest/people/', include('networkapi.people.urls')),
    url(r'^rest/opportunities/', include('networkapi.opportunities.urls')),
    url(r'^rest/news/', include('networkapi.news.urls')),
    url("^$", direct_to_template, {"template": "index.html"}, name="home"),
    url("^", include("mezzanine.urls")),
]

handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"

if settings.USE_S3 is not True:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
