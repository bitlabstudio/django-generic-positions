"""Tests for the template tags of the ``generic_positions`` app."""
from django.contrib.admin.sites import AdminSite
from django.contrib.admin.views.main import ChangeList
from django.template import Context, Template
from django.test import TestCase
from django.test.client import RequestFactory

from ..admin import GenericPositionsAdmin
from .factories import DummyModelFactory
from .test_app.models import DummyModel


class PositionResultListTestCase(TestCase):
    """Tests for the ``position_result_list`` tag."""
    longMessage = True

    def setUp(self):
        self.first_model = DummyModelFactory()
        DummyModelFactory(name='Foobar2')
        DummyModelFactory(name='Foobar3')

    def test_render_tag(self):
        request = RequestFactory().get('/')
        t = Template('{% load position_tags %}{% position_result_list cl %}')
        change_list = ChangeList(
            request=request, model=DummyModel, list_display=['name'],
            list_display_links=None, list_filter=None, date_hierarchy=None,
            search_fields=None, list_select_related=None, list_per_page=100,
            list_max_show_all=None, list_editable=None,
            model_admin=GenericPositionsAdmin(DummyModel, AdminSite()))
        change_list.formset = None
        c = Context({'cl': change_list})
        self.assertIn('name="position-{0}"'.format(self.first_model.id),
                      t.render(c))
