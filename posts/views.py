# posts/views.py
"""Views for the posts API."""

from rest_framework import viewsets, permissions

from .models import Post
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """A ViewSet for viewing and editing post instances."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def perform_create(self, serializer):
        """Ensure the post is created with the current user as the owner."""
        serializer.save(owner=self.request.user)
