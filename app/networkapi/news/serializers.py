from rest_framework import serializers

from networkapi.news.models import News


class NewsSerializer(serializers.ModelSerializer):
    """
    Serializes a News object
    """
    topic = serializers.StringRelatedField()

    class Meta:
        model = News
        fields = (
            'headline',
            'outlet',
            'date',
            'link',
            'excerpt',
            'author',
            'glyph',
            'topic',
            'featured',
        )
