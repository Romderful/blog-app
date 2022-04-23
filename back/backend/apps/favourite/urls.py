"""Favourite's urls."""


from rest_framework.routers import SimpleRouter
from .views import FavouriteViewSet


router = SimpleRouter()
router.register("", FavouriteViewSet, basename="favourite")

urlpatterns = router.urls
