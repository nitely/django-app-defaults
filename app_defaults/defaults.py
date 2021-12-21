# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import importlib
import pkgutil
import collections
import os
import inspect

from django.utils.module_loading import import_string
from django.conf import settings as django_settings

__all__ = ['settings', 'Settings']

_SCRIPT_DIR = os.getcwd()


def _from_locals(apps):
    """Return apps that lives in the local dir (i.e not python packages)"""
    return [
        app for app in apps
        if os.path.isdir(os.path.join(_SCRIPT_DIR, *app.split('.')))]


class Settings:
    """
    Get a setting from django settings or\
    app defaults. In that order

    :param list apps: List of apps to search for a ``defaults`` module.\
    It's usually a subset of the ``INSTALLED_APPS`` setting. The order matters
    :param list modules: List of module objects to lookup for settings
    :param bool locals_only: This is ``False`` by default,\
    mainly because it only works when the app's path\
    is relative to the running script. It's considered\
    better to pass the list of local ``apps`` instead or\
    make use of ``check_magic_var``. This may be deprecated\
    in the future
    :param bool check_magic_var: This checks the magic var\
    ``DEFAULT_SETTINGS_MODULE = True`` is present in\
    each app ``defaults`` module. If the var is ``False`` or\
    does not exists, then the module is ignored.
    """

    def __init__(self, apps=None, modules=None, locals_only=False, check_magic_var=False):
        apps = apps or []
        modules = modules or []
        defaults = collections.OrderedDict()
        if locals_only:
            apps = _from_locals(apps)
        for app in apps:
            try:  # handle AppConfig
                if inspect.isclass(import_string(app)):
                    app = app.rsplit('.', 2)[0]
            except ImportError:
                pass
            module = '.'.join((app, 'defaults'))
            if pkgutil.find_loader(module) is None:
                continue
            m = importlib.import_module(module)
            has_magic_var = getattr(m, 'DEFAULT_SETTINGS_MODULE', False)
            if check_magic_var and not has_magic_var:
                continue
            defaults[app] = m
        for module in modules:
            defaults[module.__file__] = module
        self._defaults = defaults

    def __getattr__(self, item):
        try:
            return getattr(django_settings, item)
        except AttributeError as err:
            for d in self._defaults.values():
                try:
                    return getattr(d, item)
                except AttributeError:
                    pass
            raise err


#: A :py:class:`.Settings` instance.
#: All installed apps with a ``defaults`` module
#: and a ``DEFAULT_SETTINGS_MODULE = True``
#: var are loaded
settings = Settings(
    apps=django_settings.INSTALLED_APPS,
    check_magic_var=True)
