"""Favourite's serializers."""

from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Favourite


class FavouriteSerializer(serializers.ModelSerializer):
    """Favourite's serializer."""

    user = serializers.SlugRelatedField(
        queryset=get_user_model().objects.all(), slug_field="username"
    )

    class Meta:
        """Meta class."""

        model = Favourite
        fields = "__all__"
