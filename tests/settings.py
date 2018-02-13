# -*- coding: utf-8 -*-

# for testing purposes
SETTING_BAR = 'bar'

SECRET_KEY = 'secret'

INSTALLED_APPS = [
    'tests.apps.app_a',
    'tests.apps.app_d'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}
