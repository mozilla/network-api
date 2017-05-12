"""Serialize the models"""
from rest_framework import serializers
from pulseapi.userprofile.models import UserBookmark


class UserBookmarkSerializer(serializers.ModelSerializer):
    """
    Serializes a {user,entry,when} bookmark.
    """

    class Meta:
        """
        Meta class. Again: because
        """
        model = UserBookmark


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializes an UserProfile...
    """

    email = serializers.EmailField()
    name = serializers.CharField(max_length=1000)
    is_staff = serializers.BooleanField(default=False)
