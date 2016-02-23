"""URLs for the ``generic_positions`` app."""
from django.conf.urls import url

from .views import PositionBulkUpdateView


urlpatterns = [
    url(r'update/$',
        PositionBulkUpdateView.as_view(),
        name='position_bulk_update'),
]
