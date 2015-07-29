# -*- coding: utf-8 -*-
"""Test Setup of ps.plone.realestatefont."""

# python imports
try:
    import unittest2 as unittest
except ImportError:
    import unittest

# zope imports
from plone import api
from plone.browserlayer.utils import registered_layers

# local imports
from ps.plone.realestatefont import (
    config,
    testing,
)


CSS = [
    '++resource++ps.plone.realestatefont/main.css',
]

JS = [
    '++resource++ps.plone.realestatefont/main.js',
]


class TestSetup(unittest.TestCase):
    """Validate setup process for ps.plone.realestatefont."""

    layer = testing.PS_PLONE_REALESTATEFONT_INTEGRATION_TESTING

    def setUp(self):
        """Additional test setup."""
        self.portal = self.layer['portal']

    def test_product_is_installed(self):
        """Validate that our product is installed."""
        qi = self.portal.portal_quickinstaller
        self.assertTrue(qi.isProductInstalled(config.PROJECT_NAME))

    def test_addon_layer(self):
        """Validate that the browserlayer for our product is installed."""
        layers = [l.getName() for l in registered_layers()]
        self.assertIn('IRealestatefontLayer', layers)


class UninstallTestCase(unittest.TestCase):

    layer = testing.PS_PLONE_REALESTATEFONT_INTEGRATION_TESTING

    def setUp(self):
        """Additional test setup."""
        self.portal = self.layer['portal']

        qi = self.portal.portal_quickinstaller
        with api.env.adopt_roles(['Manager']):
            qi.uninstallProducts(products=[config.PROJECT_NAME])

    def test_product_is_uninstalled(self):
        """Validate that our product is uninstalled."""
        qi = self.portal.portal_quickinstaller
        self.assertFalse(qi.isProductInstalled(config.PROJECT_NAME))

    def test_addon_layer_removed(self):
        """Validate that the browserlayer is removed."""
        layers = [l.getName() for l in registered_layers()]
        self.assertNotIn('IRealestatefontLayer', layers)
