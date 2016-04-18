"""Tests for the template tags of the ``generic_positions`` app."""
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.sites import AdminSite
from django.contrib.admin.views.main import ChangeList
from django.template import Context, Template
from django.test import TestCase
from django.test.client import RequestFactory

from mixer.backend.django import mixer

from ..admin import GenericPositionsAdmin
from ..templatetags.position_tags import order_by_position
from .test_app.models import DummyModel


class PositionResultListTestCase(TestCase):
    """Tests for the ``position_result_list`` tag."""
    longMessage = True

    def setUp(self):
        self.first_model = mixer.blend('test_app.DummyModel')
        mixer.blend('test_app.DummyModel')
        mixer.blend('test_app.DummyModel')

    def test_render_tag(self):
        request = RequestFactory().get('/')
        t = Template('{% load position_tags %}{% position_result_list cl %}')
        change_list = ChangeList(
            request=request, model=DummyModel, list_display=['name'],
            list_display_links=None, list_filter=None, date_hierarchy=None,
            search_fields=None, list_select_related=None, list_per_page=100,
            list_max_show_all=10, list_editable=None,
            model_admin=GenericPositionsAdmin(DummyModel, AdminSite()))
        change_list.formset = None
        c = Context({'cl': change_list})
        self.assertIn('name="position-{0}"'.format(self.first_model.id),
                      t.render(c))


class PositionInputTestCase(TestCase):
    """Tests for the ``position_input`` tag."""
    longMessage = True

    def setUp(self):
        self.first_model = mixer.blend('test_app.DummyModel')

    def test_render_tag(self):
        t = Template('{% load position_tags %}{% position_input obj %}')
        c = Context({'obj': self.first_model})
        self.assertIn('name="position-{0}"'.format(self.first_model.id),
                      t.render(c))


class OrderByPositionTestCase(TestCase):
    """Tests for the ``order_by_position`` filter."""
    longMessage = True

    def setUp(self):
        self.first_model = mixer.blend(
            'generic_positions.ObjectPosition',
            object_id=mixer.blend('test_app.DummyModel').pk,
            content_type=ContentType.objects.get_for_model(DummyModel),
            position=1).content_object
        mixer.blend('test_app.DummyModel')
        self.last_model = mixer.blend(
            'generic_positions.ObjectPosition',
            object_id=mixer.blend('test_app.DummyModel').pk,
            content_type=ContentType.objects.get_for_model(DummyModel),
            position=2).content_object

    def test_tag(self):
        qs = DummyModel.objects.all()
        self.assertEqual(qs.count(), 3)
        self.assertEqual(qs[0].name, self.first_model.name)
        order_by_position(qs)
        order_by_position(DummyModel.objects.all(), reverse='reverse')
        self.assertFalse(order_by_position(None))
