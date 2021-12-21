# -*- coding: utf-8 -*-

from django.contrib.admin.apps import AdminConfig

class MyAdminConfig(AdminConfig):
    default_site = 'tests.apps.app_f.admin.MyAdminSite'
