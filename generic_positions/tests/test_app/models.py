"""Dummy models to be used in test cases of the ``generic_positions`` app."""
from django.contrib.contenttypes import generic
from django.db import models

from ...models import ObjectPosition


class DummyModel(models.Model):
    """Dummy to be used in test cases of the ``generic_positions`` app."""
    name = models.CharField(max_length=256, blank=True)

DummyModel.add_to_class(
    'generic_position', generic.GenericRelation(ObjectPosition))
