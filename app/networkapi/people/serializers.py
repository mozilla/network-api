from rest_framework import serializers

from networkapi.people.models import (
    Person,
    Link,
    Team,
    Affiliation,
    InternetHealthIssue,
)


class LinkSerializer(serializers.ModelSerializer):
    """
    Serializes a Link Model
    """
    class Meta:
        model = Link
        fields = (
            'url',
            'name',
        )


class PersonSerializer(serializers.ModelSerializer):
    """
    Serializes a Person with Links and Teams included
    """
    teams = serializers.StringRelatedField(many=True)
    affiliations = serializers.StringRelatedField(many=True)
    internet_health_issues = serializers.StringRelatedField(many=True)
    links = LinkSerializer(many=True)

    class Meta:
        model = Person
        fields = (
            'name',
            'role',
            'location',
            'image',
            'teams',
            'links',
            'bio',
            'quote',
            'affiliations',
            'internet_health_issues',
            'partnership_logo'
        )
