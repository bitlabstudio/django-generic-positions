"""Tests for the models of the ``generic_positions`` app."""
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase

from mixer.backend.django import mixer

from ..models import ObjectPosition, save_positions
from .test_app.models import DummyModel


class ObjectPositionTestCase(TestCase):
    """Tests for the ``ObjectPosition`` model class."""
    longMessage = True

    def test_instantiation(self):
        """Test instatiation of the ``ObjectPosition`` model."""
        object_position = ObjectPosition()
        self.assertTrue(object_position)

    def test_save_positions_function(self):
        """Test the ``save_positions`` function."""
        object_position = mixer.blend(
            'generic_positions.ObjectPosition',
            content_type=ContentType.objects.get_for_model(DummyModel))
        object_position2 = mixer.blend(
            'generic_positions.ObjectPosition',
            content_type=ContentType.objects.get_for_model(DummyModel))
        post_data = {
            'position-{0}'.format(object_position.id): '2',
            'position-invalid': '2',
        }
        save_positions(post_data)

        # The obj in our dict should be updated...
        self.assertEqual(
            ObjectPosition.objects.get(id=object_position.id).position, 2)

        # ..the other one should remain the same.
        self.assertEqual(
            ObjectPosition.objects.get(id=object_position2.id).position,
            object_position2.position)
