# -*- coding: utf-8 -*-
"""Post install import steps for ps.plone.realestatefont."""

# zope imports
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            'ps.plone.realestatefont:install-base',
            'ps.plone.realestatefont:uninstall',
            'ps.plone.realestatefont:uninstall-base',
        ]
