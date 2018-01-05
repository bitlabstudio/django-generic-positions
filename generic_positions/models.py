"""Models for the ``generic_positions`` app."""
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import fields
from django.db import models
from django.utils.translation import ugettext_lazy as _


class ObjectPosition(models.Model):
    """
    Model to add a position field to any kind of object.

    :content_object: Object, which now has a position field.
    :position: Current position integer of the object.

    """
    # Generic Foreign Key Bundle
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
    )

    object_id = models.PositiveIntegerField()

    content_object = fields.GenericForeignKey()

    # Other fields
    position = models.PositiveIntegerField(
        verbose_name=_('Position'),
        null=True, blank=True,
    )


def save_positions(post_data, queryset=None):
    """
    Function to update a queryset of position objects with a post data dict.

    :post_data: Typical post data dictionary like ``request.POST``, which
      contains the keys of the position inputs.
    :queryset: Queryset of the model ``ObjectPosition``.

    """
    if not queryset:
        queryset = ObjectPosition.objects.all()
    for key in post_data:
        if key.startswith('position-'):
            try:
                obj_id = int(key.replace('position-', ''))
            except ValueError:
                continue
            queryset.filter(pk=obj_id).update(position=post_data[key])
