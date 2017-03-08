from rest_framework import serializers

from networkapi.people.models import (
    Person,
    Link,
    Team,
)

class PersonSerializer(serializers.ModelSerializer):
    """
    Serializes a Person with Links and Teams included
    """
    teams = serializers.StringRelatedField(many=True)
    links = serializers.StringRelatedField(many=True)

    class Meta:
        model = Person
        fields = (
            'name',
            'role',
            'location',
            'image',
            'teams',
            'links',
        )
