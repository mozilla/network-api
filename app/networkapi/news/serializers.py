from rest_framework import serializers

from networkapi.news.models import News


class OpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = News
