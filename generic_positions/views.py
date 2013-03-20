"""Views for the ``generic_positions`` app."""
from django.http import HttpResponse
from django.views.generic import View

from .models import ObjectPosition, save_positions


class PositionBulkUpdateView(View):
    """View to update position objects with a POST dictionary."""
    model = ObjectPosition

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            save_positions(request.POST)
        return HttpResponse('done')
