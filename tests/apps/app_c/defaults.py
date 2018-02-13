# -*- coding: utf-8 -*-

from django.conf import settings

# note: once this module is loaded,
# APP_C_IS_BAR won't change, even if
# SETTING_BAR changes, this is true
# for regular django settings al well.
# i.e the module is not reloaded,
# since that would have undesired side effects
APP_C_IS_BAR = settings.SETTING_BAR == 'bar'
