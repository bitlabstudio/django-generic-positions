"""Dummy models to be used in test cases of the ``generic_positions`` app."""
from django.db import models


class DummyModel(models.Model):
    """Dummy to be used in test cases of the ``generic_positions`` app."""
    name = models.CharField(max_length=256, blank=True)
