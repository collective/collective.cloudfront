# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from collective.cloudfront.testing import COLLECTIVE_CLOUDFRONT_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.cloudfront is properly installed."""

    layer = COLLECTIVE_CLOUDFRONT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.cloudfront is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.cloudfront'))

    def test_browserlayer(self):
        """Test that ICollectiveCloudfrontLayer is registered."""
        from collective.cloudfront.interfaces import (
            ICollectiveCloudfrontLayer)
        from plone.browserlayer import utils
        self.assertIn(ICollectiveCloudfrontLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_CLOUDFRONT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.cloudfront'])

    def test_product_uninstalled(self):
        """Test if collective.cloudfront is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.cloudfront'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveCloudfrontLayer is removed."""
        from collective.cloudfront.interfaces import \
            ICollectiveCloudfrontLayer
        from plone.browserlayer import utils
        self.assertNotIn(ICollectiveCloudfrontLayer, utils.registered_layers())
