# -*- coding: utf-8 -*-
"""Test Layer for ps.fonts.iconmagic."""

# zope imports
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
    PLONE_FIXTURE,
    applyProfile,
)
from plone.testing import (
    Layer,
    z2,
)
from zope.configuration import xmlconfig


class PsfontsIconmagicLayer(PloneSandboxLayer):
    """Custom Test Layer for ps.fonts.iconmagic."""
    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        """Set up Zope for testing."""
        # Load ZCML
        import ps.fonts.iconmagic
        xmlconfig.file(
            'configure.zcml',
            ps.fonts.iconmagic,
            context=configurationContext
        )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ps.fonts.iconmagic:default')


PS_fonts_ICONMAGIC_FIXTURE = PsfontsIconmagicLayer()


PS_fonts_ICONMAGIC_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PS_fonts_ICONMAGIC_FIXTURE,),
    name='PsfontsIconmagicLayer:IntegrationTesting'
)


PS_fonts_ICONMAGIC_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PS_fonts_ICONMAGIC_FIXTURE,),
    name='PsfontsIconmagicLayer:FunctionalTesting'
)


PS_fonts_ICONMAGIC_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PS_fonts_ICONMAGIC_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PsfontsIconmagicLayer:AcceptanceTesting'
)


ROBOT_TESTING = Layer(name='ps.fonts.iconmagic:Robot')
