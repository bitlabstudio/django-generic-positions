"""URLs for the ``generic_positions`` app."""
from django.conf.urls import patterns, url

from .views import PositionBulkUpdateView


urlpatterns = patterns(
    '',
    url(r'update/$',
        PositionBulkUpdateView.as_view(),
        name='position_bulk_update'),
)
