"""Admin classes for the ``test_app`` app."""
from django.contrib import admin

from ...admin import GenericPositionsAdmin
from .models import DummyModel


admin.site.register(DummyModel, GenericPositionsAdmin)
