"""Admin classes for the ``generic_positions`` app."""
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType

from .models import ObjectPosition


class GenericPositionsAdmin(admin.ModelAdmin):
    """Admin to let models be dragged & dropped with jQuery UI sortable."""
    change_list_template = 'generic_positions/admin/change_list.html'
    ordering = ('generic_position__position', )

    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            '//ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'generic_positions/js/reorder.js',
        )

    def save_model(self, request, obj, form, change):
        """Add an ObjectPosition to the object."""
        super(GenericPositionsAdmin, self).save_model(request, obj, form,
                                                      change)
        c_type = ContentType.objects.get_for_model(obj)
        try:
            ObjectPosition.objects.get(content_type__pk=c_type.id,
                                       object_id=obj.id)
        except ObjectPosition.DoesNotExist:
            ObjectPosition.objects.create(content_object=obj)
