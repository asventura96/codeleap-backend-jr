# posts/serializers.py
"""Serializers for the posts app."""

from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """Serializer for the Post model."""

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Metadata options for the PostSerializer."""
        model = Post
        fields = ['id', 'owner', 'created_datetime', 'title', 'content']
