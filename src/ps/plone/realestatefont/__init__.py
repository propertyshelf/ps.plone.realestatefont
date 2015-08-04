# -*- coding: utf-8 -*-
"""Real Estate icon font."""

# python imports
import logging

# zope imports
from zope.i18nmessageid import MessageFactory

# local imports
from ps.plone.realestatefont import config

logger = logging.getLogger(config.PROJECT_NAME)
_ = MessageFactory('ps.plone.realestatefont')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
