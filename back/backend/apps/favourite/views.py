"""Favourite's views."""

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Favourite
from .serializers import FavouriteSerializer


class FavouriteViewSet(viewsets.ModelViewSet):
    """Favourite's main model viewset."""

    serializer_class = FavouriteSerializer
    queryset = Favourite.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["user", "id", "article"]
