# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.test import TestCase, override_settings

from app_defaults import Settings, settings


class DefaultsTest(TestCase):

    def setUp(self):
        pass

    def test_apps_settings(self):
        """
        Should load from apps param
        """
        s = Settings(apps=["tests.apps.app_a"])
        self.assertEqual(s.APP_A_FOO, "foo")

    def test_modules_settings(self):
        """
        Should load from modules param
        """
        from .apps.app_a import defaults
        s = Settings(modules=[defaults])
        self.assertEqual(s.APP_A_FOO, "foo")

    def test_locals_settings(self):
        """
        Should import locals only
        """
        # This param may get deprecated!
        self.assertRaises(ImportError, Settings, apps=["global_module_foo"])
        s = Settings(apps=["tests.apps.app_a", "global_module_foo"], locals_only=True)
        self.assertEqual(s.APP_A_FOO, "foo")

    def test_magic_var_settings(self):
        """
        Should filter modules with magic var check
        """
        s = Settings(apps=["tests.apps.app_a"], check_magic_var=True)
        self.assertRaises(AttributeError, lambda: s.APP_A_FOO)
        s = Settings(apps=["tests.apps.app_b"], check_magic_var=True)
        self.assertEqual(s.APP_B_FOO, "foo")

    @override_settings(APP_A_FOO="bar")
    def test_override_settings(self):
        """
        Should allow project to override default settings
        """
        s = Settings(apps=["tests.apps.app_a"])
        self.assertEqual(s.APP_A_FOO, "bar")

    def test_site_settings_is_bar(self):
        """
        Should allow defaults to import django.settings
        """
        s = Settings(apps=["tests.apps.app_c"])
        self.assertTrue(s.APP_C_IS_BAR)

    def test_settings_default(self):
        """
        Should auto load default that have a magic var
        """
        self.assertEqual(settings.APP_D_FOO, 'foo')
        self.assertRaises(AttributeError, lambda: settings.APP_A_FOO)

    def test_settings(self):
        """
        Should get settings from project
        """
        self.assertEqual(settings.SETTING_BAR, 'bar')

    def test_app_without_defaults(self):
        """
        Should ignore app without defaults
        """
        s = Settings(apps=["tests.apps.app_a", "tests.apps.app_e"])
        self.assertEqual(s.APP_A_FOO, "foo")

    def test_custom_admin(self):
        s = Settings(apps=["tests.apps.app_f.apps.MyAdminConfig"])
        self.assertEqual(s.APP_F_FOO, "foo")
