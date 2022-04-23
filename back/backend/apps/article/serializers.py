"""Article's serializers."""

from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    """Article's serializer."""

    author = serializers.SlugRelatedField(
        queryset=get_user_model().objects.all(), slug_field="username"
    )

    class Meta:
        """Meta class."""

        model = Article
        fields = "__all__"
