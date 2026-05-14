"""
This ``urls.py`` is only used when running the tests via ``runtests.py``.
As you know, every app must be hooked into yout main ``urls.py`` so that
you can actually reach the app's views (provided it has any views, of course).

"""

from django.conf.urls import include, re_path
from django.contrib import admin
from django.views.generic import ListView

from .test_app.models import DummyModel


admin.autodiscover()


urlpatterns = [
    re_path(r"^admin/", include(admin.site.urls)),
    re_path(r"^position/", include("generic_positions.urls")),
    re_path(r"$", ListView.as_view(model=DummyModel)),
]
