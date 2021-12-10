# -*- coding: utf-8 -*-
from plone import api
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller"""
        return [
            'collective.cloudfront:uninstall',
        ]


def post_install(context):
    """Post install script"""
    setup = api.portal.get_tool('portal_setup')
    setup.runImportStepFromProfile('collective.cloudfront:initial', 'rolemap')


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.