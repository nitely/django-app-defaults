# django-app-defaults

A library for managing apps and projects default static settings.
Define default settings for apps and override them in project settings when needed.

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

# `django.conf.settings` or any other module can be imported if needed

# required
DEFAULT_SETTINGS_MODULE = True

# define default settings below
MY_DEFAULT_SETTING = "yey"
```

Then anywhere within your project:

```python
from app_defaults import settings

print(settings.MY_DEFAULT_SETTING)
# yey

# All `django.conf.settings` are also available
print(settings.DEBUG)
# True
```

To load default setting for a single app instead of all of the apps, just do:

```python
settings = Settings(apps=["my_app"])

# or

from my_app import defaults
settings = Settings(modules=[defaults])
```

> Note: the `DEFAULT_SETTINGS_MODULE`` variable is not required
> when explicitly passing the `apps` or `modules`

## How it works

It's an extremely simple library. It goes through all installed apps and
looks for a `defaults.py` module at the root of the app. If a `DEFAULT_SETTINGS_MODULE`
is found, the module is loaded.

It's similar to the following pattern but generalized in a reusable lib:

```python
from my_app import defaults
from django.conf import settings

class Settings(object):
    def __getattr__(self, attr):
        try:
            return getattr(settings, attr)
        except AttributeError:
            return getattr(defaults, attr)
```

## Documentation

N/A

## License

MIT
