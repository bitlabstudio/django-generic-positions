"""Factories of the ``generic_positions`` app."""
import factory

from ..models import ObjectPosition
from .test_app.models import DummyModel


class DummyModelFactory(factory.Factory):
    """Factory for the ``DummyModel`` model."""
    FACTORY_FOR = DummyModel

    name = 'Foobar'


class ObjectPositionFactory(factory.Factory):
    """Factory for the ``ObjectPosition`` model."""
    FACTORY_FOR = ObjectPosition

    content_object = factory.SubFactory(DummyModelFactory)
