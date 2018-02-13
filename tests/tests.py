# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.test import TestCase, override_settings

from app_defaults import Settings, settings


class DefaultsTest(TestCase):

    def setUp(self):
        pass

    def test_apps_settings(self):
        """
        """
        s = Settings(apps=["tests.apps.app_a"])
        self.assertEqual(s.APP_A_FOO, "foo")

    def test_modules_settings(self):
        """
        """
        from tests.apps.app_a import defaults
        s = Settings(modules=[defaults])
        self.assertEqual(s.APP_A_FOO, "foo")

    def test_locals_settings(self):
        """
        """
        self.assertRaises(ImportError, Settings, apps=["global_module_foo"])
        s = Settings(apps=["tests.apps.app_a", "global_module_foo"], locals_only=True)
        self.assertEqual(s.APP_A_FOO, "foo")

    def test_magic_var_settings(self):
        """
        """
        s = Settings(apps=["tests.apps.app_a"], check_magic_var=True)
        self.assertRaises(AttributeError, lambda: s.APP_A_FOO)
        s = Settings(apps=["tests.apps.app_b"], check_magic_var=True)
        self.assertEqual(s.APP_B_FOO, "foo")

    @override_settings(APP_A_FOO="bar")
    def test_override_settings(self):
        """
        """
        s = Settings(apps=["tests.apps.app_a"])
        self.assertEqual(s.APP_A_FOO, "bar")

    def test_site_settings_is_bar(self):
        """
        """
        s = Settings(apps=["tests.apps.app_c"])
        self.assertTrue(s.APP_C_IS_BAR)

    def test_settings(self):
        """
        """
        self.assertEqual(settings.APP_D_FOO, 'foo')
        self.assertRaises(AttributeError, lambda: settings.APP_A_FOO)
