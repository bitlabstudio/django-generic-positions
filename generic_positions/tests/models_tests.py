"""Tests for the models of the ``generic_positions`` app."""
from django.test import TestCase

from ..models import ObjectPosition
from .factories import ObjectPositionFactory


class ObjectPositionTestCase(TestCase):
    """Tests for the ``ObjectPosition`` model class."""
    longMessage = True

    def test_instantiation(self):
        """Test instatiation of the ``ObjectPosition`` model."""
        object_position = ObjectPosition()
        self.assertTrue(object_position)

        # Test factory
        object_position = ObjectPositionFactory()
        self.assertEqual(object_position.position, 5)
