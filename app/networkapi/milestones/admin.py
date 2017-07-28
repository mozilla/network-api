from django.contrib import admin

from networkapi.milestones.models import Milestone, MilestoneLink


admin.site.register(Milestone)
admin.site.register(MilestoneLink)
