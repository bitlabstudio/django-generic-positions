"""Views for the ``generic_positions`` app."""
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import requires_csrf_token
from django.views.generic import View

from .models import save_positions


class PositionBulkUpdateView(View):
    """View to update position objects with a POST dictionary."""
    http_method_names = [u'post', ]

    @method_decorator(csrf_exempt)
    @method_decorator(requires_csrf_token)
    def dispatch(self, request, *args, **kwargs):
        return super(PositionBulkUpdateView, self).dispatch(
            request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            save_positions(request.POST)
        return HttpResponse('done')
