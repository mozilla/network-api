from django.contrib import admin

from networkapi.news.models import News, Topic


admin.site.register(News)
admin.site.register(Topic)
