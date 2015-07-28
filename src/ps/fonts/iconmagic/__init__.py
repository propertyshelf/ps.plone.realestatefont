# -*- coding: utf-8 -*-
"""Propertyshelf IconMagic Font."""

# python imports
import logging

# zope imports
from zope.i18nmessageid import MessageFactory

# local imports
from ps.fonts.iconmagic import config

logger = logging.getLogger(config.PROJECT_NAME)
_ = MessageFactory('ps.fonts.iconmagic')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
