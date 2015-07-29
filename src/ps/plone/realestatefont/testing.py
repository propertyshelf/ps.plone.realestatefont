# -*- coding: utf-8 -*-
"""Test Layer for ps.plone.realestatefont."""

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


class PsPloneRealestatefontLayer(PloneSandboxLayer):
    """Custom Test Layer for ps.plone.realestatefont."""
    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        """Set up Zope for testing."""
        # Load ZCML
        import ps.plone.realestatefont
        xmlconfig.file(
            'configure.zcml',
            ps.plone.realestatefont,
            context=configurationContext
        )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ps.plone.realestatefont:default')


PS_PLONE_REALESTATEFONT_FIXTURE = PsPloneRealestatefontLayer()


PS_PLONE_REALESTATEFONT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PS_PLONE_REALESTATEFONT_FIXTURE,),
    name='PsPloneRealestatefontLayer:IntegrationTesting'
)


PS_PLONE_REALESTATEFONT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PS_PLONE_REALESTATEFONT_FIXTURE,),
    name='PsPloneRealestatefontLayer:FunctionalTesting'
)


PS_PLONE_REALESTATEFONT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PS_PLONE_REALESTATEFONT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PsPloneRealestatefontLayer:AcceptanceTesting'
)


ROBOT_TESTING = Layer(name='ps.plone.realestatefont:Robot')
