# posts/models.py
"""Data models for the posts app."""

from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """Represents a single post created by a user."""

    owner = models.ForeignKey(
        User, related_name='posts', on_delete=models.CASCADE
    )
    created_datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self) -> str:
        """Return the string representation of the post, which is its title."""
        return str(self.title)

    class Meta:
        """Metadata options for the Post model."""

        ordering = ['-created_datetime']
