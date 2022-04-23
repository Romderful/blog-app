"""Article's tests."""

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Article


class ArticleViewsetTestCase(APITestCase):
    """Article's tests."""

    def setUp(self):
        """Set up config.

        Create an article.
        """
        user = get_user_model()

        author = user.objects.create_user(
            username="test_name",
            email="test@gmail.com",
            password="some_password",
        )

        Article.objects.create(
            id=1,
            author=author,
            title="My first article",
            article_content="First test !",
        )

        Article.objects.create(
            id=2,
            author=author,
            title="My second article",
            article_content="Second test !",
        )

    def test_retrieve_article_list(self):
        """Test that all the Articles are correctly returned."""
        response = self.client.get("/api-v1/article/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Article with id 1
        self.assertEqual(response.data[0]["title"], "My first article")
        self.assertEqual(response.data[0]["article_content"], "First test !")
        # Article with id 2
        self.assertEqual(response.data[1]["title"], "My second article")
        self.assertEqual(response.data[1]["article_content"], "Second test !")

    def test_retrieve_Article_detail(self):
        """Test that a specific Article's detail is correctly returned."""
        response = self.client.get("/api-v1/article/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "My first article")
        self.assertEqual(response.data["article_content"], "First test !")
