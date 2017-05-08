# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.cloudfront


class CollectiveCloudfrontLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=collective.cloudfront)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.cloudfront:default')


COLLECTIVE_CLOUDFRONT_FIXTURE = CollectiveCloudfrontLayer()


COLLECTIVE_CLOUDFRONT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_CLOUDFRONT_FIXTURE,),
    name='CollectiveCloudfrontLayer:IntegrationTesting'
)


COLLECTIVE_CLOUDFRONT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_CLOUDFRONT_FIXTURE,),
    name='CollectiveCloudfrontLayer:FunctionalTesting'
)


COLLECTIVE_CLOUDFRONT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_CLOUDFRONT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveCloudfrontLayer:AcceptanceTesting'
)
