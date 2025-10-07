# posts/tests.py
"""API tests for the posts app."""

from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Post


class PostApiTests(APITestCase):
    """Tests for the Post API endpoints."""

    def setUp(self):
        """Set up the test environment before each test."""
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        Post.objects.create(
            owner=self.user,
            title='Post de Teste',
            content='Conteúdo de teste.'
        )

    def test_list_posts_unauthenticated(self):
        """
        Ensure anyone can list posts, even when unauthenticated.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_create_post_authenticated(self):
        """
        Ensure an authenticated user can create a new post.
        """
        self.client.login(username='testuser', password='testpassword')

        data = {
            'title': 'Novo Post Criado no Teste',
            'content': 'Conteúdo do novo post.'
        }
        response = self.client.post('/', data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)
        self.assertEqual(response.data['owner'], 'testuser')

    def test_create_post_unauthenticated(self):
        """
        Ensure an unauthenticated user cannot create a post.
        """
        data = {'title': 'Post Ilegal', 'content': 'Conteúdo.'}
        response = self.client.post('/', data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
