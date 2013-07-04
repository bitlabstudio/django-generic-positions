"""Admin classes for the ``test_app`` app."""
from django.contrib import admin

from ...admin import GenericPositionsAdmin
from .models import DummyModel, DummyParentModel


class DummyModelAdmin(GenericPositionsAdmin):
    list_filter = ('name', )


admin.site.register(DummyModel, DummyModelAdmin)
admin.site.register(DummyParentModel, GenericPositionsAdmin)
