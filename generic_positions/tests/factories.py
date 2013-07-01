"""Factories of the ``generic_positions`` app."""
import factory

from ..models import ObjectPosition
from .test_app.models import DummyModel, DummyParentModel


class DummyParentModelFactory(factory.Factory):
    """Factory for the ``DummyParentModel`` model."""
    FACTORY_FOR = DummyParentModel

    name = 'Foobar'


class DummyModelFactory(factory.Factory):
    """Factory for the ``DummyModel`` model."""
    FACTORY_FOR = DummyModel

    name = 'Foobar'
    parent = factory.SubFactory(DummyParentModelFactory)


class ObjectPositionFactory(factory.Factory):
    """Factory for the ``ObjectPosition`` model."""
    FACTORY_FOR = ObjectPosition

    content_object = factory.SubFactory(DummyModelFactory)
