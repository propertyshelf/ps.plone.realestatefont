# -*- coding: utf-8 -*-
"""Zope2 install and uninstall."""

# local imports
from ps.fonts.iconmagic import (
    config,
    logger,
)


def uninstall(portal, reinstall=False):
    """Uninstall the add-on."""
    if not reinstall:
        setup_tool = portal.portal_setup
        setup_tool.runAllImportStepsFromProfile(
            '{0}:uninstall'.format(config.PROFILE_ID)
        )
        logger.info('Uninstall done')
