Django Generic Positions
========================

This is a generic app for using a drag & drop position field, wherever you want
to.

You often have items that should have a position field so that the user
can manipulate their ordering by entering intergers into that field. This app
allows you to easily add drag and drop functionality to that model's Django
admin or even to your frontend.

You don't need to manipulate your models, which means that you can even make
third party models that don't have a position field at all position aware.

Prerequisites
-------------

You need at least the following packages in your virtualenv:

* Django 1.4
* South


Installation
------------

To get the latest stable release from PyPi::

    $ pip install django-generic-positions

To get the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/django-generic-positions.git#egg=generic_positions

Add the app to your ``INSTALLED_APPS``::

    INSTALLED_APPS = [
        ...
        'generic_positions',
    ]

Add this to your main ``urls.py``::

    urlpatterns = patterns(
        '',
        url(r'^pos/', include('generic_positions.urls')),
        ...
    )

Run the south migrations to create the app's database tables::

    $ ./manage.py migrate generic_positions

Usage
-----

If you want to add the position feature to the model of a third party app,
do the following in one of your ``models.py`` files::

    from django.contrib.contenttypes import generic
    from thirdpartyapp.models import TheModel

    TheModel.add_to_class(
        'generic_position',
        generic.GenericRelation('generic_positions.ObjectPosition'),
    )

If you are extending on of your own models, simply add this to your model::

    from django.contrib.contenttypes import generic

    class YourModel(models.Model):
        ...
        generic_position = generic.GenericRelation(
            'generic_positions.ObjectPosition'
        )

IMPORTANT. If you are using multiple models, which have generic relations to
the positioning model, this is what you should NOT do: For some reason there
will be duplicates of your model appearing in the templates. Please don't use
``ordering = ['generic_position__position']``.


Usage in templates
++++++++++++++++++

There are several template tags and filters you can use. Let's start with a
simple view, which orders the object list by position::

    {% load position_tags %}
    {% for obj in object_list|order_by_position %}
        <p>{{ obj }}</p>
    {% endfor %}

You want to reverse the ordering? Go for it::

    {% load position_tags %}
    {% for obj in object_list|order_by_position:'reverse' %}
        <p>{{ obj }}</p>
    {% endfor %}

Let's show the current position, too::

    {% load position_tags %}
    {% for obj in object_list|order_by_position:'reverse' %}
        <p>{% position_input obj 'visible' %} &raquo; {{ obj }}</p>
    {% endfor %}

The ``position_input`` tag will add a hidden field with the position nr. and
if you add ``visible`` it will also append a span element.

If you also want the drag & drop functionality, have a look at the following
example of a complete implementation::

    {% load position_tags %}
    <form method="post" action="{% url "position_bulk_update" %}">
        {% csrf_token %}
        <ul id="positionContainer">
            {% for obj in object_list|order_by_position %}
                <li>{{ obj }}{% position_input obj %}</li>
            {% endfor %}
        </ul>
    </form>

    # You might want to place these scripts in your base template
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.7.0/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="{{ STATIC_URL }}js/libs/jquery.min.js"><\/script>')</script>
    <script src="//ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js"></script>
    <script>window.jQuery || document.write('<script src="{{ STATIC_URL }}js/libs/jquery-ui.min.js"><\/script>')</script>
    <script type="text/javascript" src="{{ STATIC_URL }}generic_positions/js/reorder.js"></script>

A few things are important here:

* You must put a form around your position aware objects
* The form must POST to the url ``position_bulk_update``
* Don't forget to add the ``csrf_token``
* Inside the form you need a wrapper element that wraps all your position aware
  items. A ``<ul id="positionContainer">`` tag is usually recommended.
* Make sure that your wrapper element has the ID ``positionContainer``.
* Next to each of your position items you need to render a hidden field with
  its current position, that can be posted to the form. Use the template tag
  ``{% position_input obj %}`` to automatically add the right input field.

Usage with Django Admin
+++++++++++++++++++++++

If you want to use the drag & drop positioning in the Django admin use::

    from generic_positions.admin import GenericPositionsAdmin
    admin.site.register(YOUR_MODEL, GenericPositionsAdmin)


Roadmap
-------

See the issue tracker for current and upcoming features.
