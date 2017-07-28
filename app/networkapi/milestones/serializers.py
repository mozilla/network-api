from rest_framework import serializers

from networkapi.milestones.models import Milestone, MilestoneLink


class MilestoneLinkSerializer(serializers.ModelSerializer):
    """
    Serializes a MilestoneLink object
    """
    class Meta:
        model = MilestoneLink
        fields = (
            'label',
            'url'
        )


class MilestoneSerializer(serializers.ModelSerializer):
    """
    Serializes a Milestone object
    """
    link = MilestoneLinkSerializer()

    class Meta:
        model = Milestone
        fields = (
            'id',
            'link',
            'headline',
            'photo',
            'start_date',
            'end_date',
            'description'
        )
