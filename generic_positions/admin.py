"""Admin classes for the ``generic_positions`` app."""
from django.contrib import admin
from django.contrib.admin.options import csrf_protect_m

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

    @csrf_protect_m
    def changelist_view(self, request, **kwargs):
        resp = super(GenericPositionsAdmin, self).changelist_view(
            request, **kwargs)
        if request.method == "POST":
            for key in request.POST:
                if key.startswith('position-'):
                    try:
                        obj_id = key.replace('position-', '')
                    except ValueError:
                        continue
                    ObjectPosition.objects.filter(pk=obj_id).update(
                        position=request.POST[key])
        return resp
