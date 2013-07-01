"""Admin classes for the ``test_app`` app."""
from django.contrib import admin

from ...admin import GenericPositionsAdmin
from .models import DummyModel, DummyParentModel


admin.site.register(DummyModel, GenericPositionsAdmin)
admin.site.register(DummyParentModel, GenericPositionsAdmin)
