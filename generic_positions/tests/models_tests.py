"""Tests for the models of the ``generic_positions`` app."""
from django.test import TestCase

from ..models import ObjectPosition


class ObjectPositionTestCase(TestCase):
    """Tests for the ``ObjectPosition`` model class."""
    longMessage = True

    def test_instantiation(self):
        """Test instatiation of the ``ObjectPosition`` model."""
        object_position = ObjectPosition()
        self.assertTrue(object_position)
