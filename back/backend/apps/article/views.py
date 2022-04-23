"""Article's views."""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Article
from .serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """Article's main model viewset."""

    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Article.objects.all()
