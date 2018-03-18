# django-app-defaults

[![Build Status](https://img.shields.io/travis/nitely/django-app-defaults.svg?style=flat-square)](https://travis-ci.org/nitely/django-app-defaults)
[![Coverage Status](https://img.shields.io/coveralls/nitely/django-app-defaults.svg?style=flat-square)](https://coveralls.io/r/nitely/django-app-defaults)
[![pypi](https://img.shields.io/pypi/v/django-app-defaults.svg?style=flat-square)](https://pypi.python.org/pypi/django-app-defaults)
[![licence](https://img.shields.io/pypi/l/django-app-defaults.svg?style=flat-square)](https://raw.githubusercontent.com/nitely/django-app-defaults/master/LICENSE)

A library for managing default static settings for apps and projects.
Define default settings for apps and override them in project settings when needed.

## Why?

This library encourages loose coupling between apps by defining
the settings of each app locally. For authors of reusable apps,
it allows to avoid the `getattr` pattern, and the definition of
default values scattered everywhere. Unlike other alternatives,
it avoids being too magical, and sticks to the Django conventions.
Defining settings should be simple, as they are just settings after all.

## Requirements

* Python 2.7, +3.4
* Django 1.8, 1.11, +2.0

## Install

```
pip install django-app-defaults
```

## Usage

```python
# my_app/defaults.py

# `django.conf.settings` or any other
# module can be imported and used

# required for auto discoverability
DEFAULT_SETTINGS_MODULE = True

#: This is a doc comment for
#: my setting I just created
MY_DEFAULT_SETTING = "yay"
```

> Note: all `defaults`'s settings can be
> overridden in `my_project/settings.py`

Then anywhere within your project or app:

```python
from app_defaults import settings

print(settings.MY_DEFAULT_SETTING)
# yay

# All `django.conf.settings` are also available
print(settings.DEBUG)
# True
```

To load default settings for a single app instead of all of the apps, just do:

```python
from app_defaults import Settings

settings = Settings(apps=["my_app"])

# or

from my_app import defaults
settings = Settings(modules=[defaults])
```

> Note: the `DEFAULT_SETTINGS_MODULE` variable is not required
> when explicitly passing `apps` or `modules`

## How it works

It's an extremely simple library. It goes through all installed apps and
looks for a `defaults.py` module at the root of the app. If a `DEFAULT_SETTINGS_MODULE`
var is found, then the module is loaded.

It's similar to the following pattern, but generalized into a reusable lib:

```python
from my_app import defaults
from django.conf import settings

class Settings:
    def __getattr__(self, attr):
        try:
            return getattr(settings, attr)
        except AttributeError:
            return getattr(defaults, attr)
```

## Documentation

[django-app-defaults.readthedocs.io](http://django-app-defaults.readthedocs.io)

## Tests

```
make test
```

## License

MIT
