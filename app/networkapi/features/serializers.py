from rest_framework import serializers

from networkapi.features.models import Feature


class FeatureSerializer(serializers.ModelSerializer):
    """
    Serializes an Feature Model
    """
    link = serializers.SerializerMethodField()

    def get_link(self, feature):
        return {
            'label': feature.link_label,
            'url': feature.link_url,
        }

    class Meta:
        model = Feature
        fields = (
            'name',
            'description',
            'link',
            'featured',
            'image'
        )
