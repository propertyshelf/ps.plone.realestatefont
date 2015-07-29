# -*- coding: utf-8 -*-
"""Common interface definitions for ps.plone.realestatefont."""

# zope imports
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IRealestatefontLayer(IDefaultBrowserLayer):
    """Marker interface that defines a Zope 3 browser layer."""
