# -*- coding: utf-8 -*-
"""Real Estate icon font."""

# python imports
import logging

# zope imports
try:
    from zope.i18nmessageid import MessageFactory
except ImportError:
    pass
else:
    _ = MessageFactory('ps.plone.realestatefont')

# local imports
from ps.plone.realestatefont import config

logger = logging.getLogger(config.PROJECT_NAME)


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
