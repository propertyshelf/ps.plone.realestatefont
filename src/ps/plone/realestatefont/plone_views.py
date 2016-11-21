# -*- coding: utf-8 -*-

# zope imports
from Products.Five import BrowserView
from plone import api as ploneapi


PLONE_5 = '5' <= ploneapi.env.plone_version() < '6'


class FontPreview(BrowserView):
    """View to preview the font."""

    def __call__(self):
        self.setup()
        return super(FontPreview, self).__call__()

    def setup(self):
        if PLONE_5:
            from Products.CMFPlone.resources import add_resource_on_request
            add_resource_on_request(self.request, 'psplonerealestatefont')
