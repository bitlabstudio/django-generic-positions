Django Generic Positions
========================

Generic app for using a drag & drop position field, wherever you want to.

We have a million places where we add position fields to models, but then we
rarely ever use them, because they are a pain in the ass to manage.

Scenario:
If you want something to become the new first item, you'll have to change the
numbers for all items or at least create a post_save function to do this
automatically.

How about dragging it? That's what you want, right?

Prerequisites
-------------

You need at least the following packages in your virtualenv:

* Django 1.4
* South


Installation
------------

To get the latest stable release from PyPi::

    $ pip install django-generic-positions (not available at the moment)

To get the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/django-generic-positions.git#egg=generic_positions

Add the app to your ``INSTALLED_APPS``::

    INSTALLED_APPS = [
        ...
        'generic_positions',
    ]

Run the south migrations to create the app's database tables::

    $ ./manage.py migrate generic_positions


Usage
-----

Let the desired models inherit from ``GenericPositionsModel``::

    from generic_positions.models import GenericPositionsModel

    class YOUR_MODEL(GenericPositionsModel):
        class Meta:
            ordering = ['generic_position__position']

Don't forget to add the ordering, right?

If you want to use the drag & drop positioning in the Django admin use::

    from generic_positions.admin import GenericPositionsAdmin
    admin.site.register(YOUR_MODEL, GenericPositionsAdmin)


Roadmap
-------

See the issue tracker for current and upcoming features.
