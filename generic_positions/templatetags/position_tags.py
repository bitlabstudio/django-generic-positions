"""Template tags of the ``generic_positions`` app."""
from django.contrib.admin.templatetags.admin_list import result_list
from django.contrib.contenttypes.models import ContentType
from django.template import Library
from django.utils.safestring import mark_safe

from ..models import ObjectPosition

register = Library()


@register.filter()
def order_by_position(qs, reverse=False):
    """Template filter to return a position-ordered queryset."""
    if qs:
        # ATTENTION: Django creates an invalid sql statement if two related
        # models have both generic positions, so we cannot use
        # qs.oder_by('generic_position__position')
        position = 'position'
        if reverse:
            position = '-' + position
        # Get content type of first queryset item
        c_type = ContentType.objects.get_for_model(qs[0])
        # Check that every item has a valid position item
        for obj in qs:
            ObjectPosition.objects.get_or_create(
                content_type=c_type, object_id=obj.pk)
        return [
            o.content_object for o in ObjectPosition.objects.filter(
                content_type=c_type, object_id__in=qs).order_by(position)
        ]
    return qs


@register.inclusion_tag('generic_positions/position.html')
def position_input(obj, visible=False):
    """Template tag to return an input field for the position of the object."""
    if not obj.generic_position.all():
        ObjectPosition.objects.create(content_object=obj)
    return {'obj': obj, 'visible': visible,
            'object_position': obj.generic_position.all()[0]}


@register.inclusion_tag('admin/change_list_results.html')
def position_result_list(change_list):
    """
    Returns a template which iters through the models and appends a new
    position column.

    """
    result = result_list(change_list)
    # Remove sortable attributes
    for x in range(0, len(result['result_headers'])):
        result['result_headers'][x]['sorted'] = False
        if result['result_headers'][x]['sortable']:
            result['result_headers'][x]['class_attrib'] = mark_safe(
                ' class="sortable"')
    # Append position <th> element
    result['result_headers'].append({
        'url_remove': '?o=',
        'sort_priority': 1,
        'sortable': True,
        'class_attrib': mark_safe(' class="sortable sorted ascending"'),
        'sorted': True,
        'text': 'position',
        'ascending': True,
        'url_primary': '?o=-1',
        'url_toggle': '?o=-1',
    })
    # Append the editable field to every result item
    for x in range(0, len(result['results'])):
        obj = change_list.result_list[x]
        # Get position object
        c_type = ContentType.objects.get_for_model(obj)
        try:
            object_position = ObjectPosition.objects.get(
                content_type__pk=c_type.id, object_id=obj.id)
        except ObjectPosition.DoesNotExist:
            object_position = ObjectPosition.objects.create(content_object=obj)
        # Add the <td>
        html = ('<td><input class="vTextField" id="id_position-{0}"'
                ' maxlength="10" name="position-{0}" type="text"'
                ' value="{1}" /></td>').format(object_position.id,
                                               object_position.position)
        result['results'][x].append(mark_safe(html))
    return result
