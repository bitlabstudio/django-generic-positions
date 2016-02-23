"""
This ``urls.py`` is only used when running the tests via ``runtests.py``.
As you know, every app must be hooked into yout main ``urls.py`` so that
you can actually reach the app's views (provided it has any views, of course).

"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import ListView

from .test_app.models import DummyModel


admin.autodiscover()


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^position/', include('generic_positions.urls')),
    url(r'$', ListView.as_view(model=DummyModel)),
]
