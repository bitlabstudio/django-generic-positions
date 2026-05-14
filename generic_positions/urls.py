"""URLs for the ``generic_positions`` app."""

from django.conf.urls import re_path

from .views import PositionBulkUpdateView


urlpatterns = [
    re_path(r"update/$", PositionBulkUpdateView.as_view(), name="position_bulk_update"),
]
