"""Favourite's models."""

from ..article.models import Article
from django.contrib.auth import get_user_model
from django.db import models


class Favourite(models.Model):
    """Favourite's table."""

    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    article = models.ForeignKey(Article, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """Display the title and the state of the Favourite in the admin panel."""
        return f"{self.user} - {self.article}"
