# posts/apps.py
"""Configuration for the posts Django app."""

from django.apps import AppConfig


class PostsConfig(AppConfig):
    """App configuration for the 'posts' app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "posts"
