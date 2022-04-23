"""Favourite's app administration."""


from django.contrib import admin
from .models import Favourite


admin.site.register(Favourite)
