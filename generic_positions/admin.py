"""Admin classes for the ``generic_positions`` app."""
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType

from .models import ObjectPosition


class GenericPositionsAdmin(admin.ModelAdmin):
    """Admin to let models be dragged & dropped with jQuery UI sortable."""
    change_list_template = 'generic_positions/admin/change_list.html'

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
            position_objects = ObjectPosition.objects.filter(
                content_type__pk=c_type.id, position__isnull=False).order_by(
                    '-position')
            try:
                position = (position_objects[0].position + 1)
            except IndexError:
                position = 1
            ObjectPosition.objects.create(
                content_object=obj, position=position)
