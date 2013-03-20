"""Tests for the views of the ``generic_positions`` app."""
from django.test import TestCase

from django_libs.tests.mixins import ViewTestMixin


class PositionBulkUpdateViewTestCase(ViewTestMixin, TestCase):
    """Tests for the ``PositionBulkUpdateView`` generic based view."""
    longMessage = True

    def get_view_name(self):
        return 'position_bulk_update'

    def test_view(self):
        self.is_callable(method='post')
        resp = self.client.post(self.get_url(),
                                HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(resp.status_code, 200)
