"""Article's models."""

from django.db import models
from django.contrib.auth import get_user_model


class Article(models.Model):
    """Article's table."""

    author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    title = models.CharField(max_length=150)
    article_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """Display the title and the state of the Article in the admin panel."""
        return f"{self.title} - {self.author}"
