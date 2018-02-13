.. _usage:

Usage
=====

Create settings
---------------

Settings must be defined within a ``defaults`` module at the root of the app:

::

    # my_app/defaults.py

    # `django.conf.settings` or any other
    # module can be imported if needed

    # required
    DEFAULT_SETTINGS_MODULE = True

    # define default settings below
    MY_DEFAULT_SETTING = "yey"

Use settings
------------

Then anywhere within your project:

::

    from app_defaults import settings

    print(settings.MY_DEFAULT_SETTING)
    # yey

    # All `django.conf.settings` are also available
    print(settings.DEBUG)
    # True

Load settings for a single app
------------------------------

    Note: the ``DEFAULT_SETTINGS_MODULE`` variable is not required
    when explicitly passing ``apps`` or ``modules``

::

    from app_defaults import Settings

    settings = Settings(apps=["my_app"])

    # or

    from my_app import defaults
    settings = Settings(modules=[defaults])

