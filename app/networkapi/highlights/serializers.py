from rest_framework import serializers

from networkapi.highlights.models import Highlight


class HighlightSerializer(serializers.ModelSerializer):
    """
    Serializes an Highlight Model
    """
    link = serializers.SerializerMethodField()

    def get_link(self, highlight):
        return {
            'label': highlight.link_label,
            'url': highlight.link_url,
        }

    class Meta:
        model = Highlight
        fields = (
            'name',
            'description',
            'link',
            'featured',
            'image'
        )
