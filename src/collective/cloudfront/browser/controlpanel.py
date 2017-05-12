from collective.cloudfront import (
    _,
    prefix,
)
from .interfaces import ICloudFrontConfiguration
from logging import getLogger
from plone.app.registry.browser import controlpanel

log = getLogger('Plone')


class CloudFrontControlPanelForm(controlpanel.RegistryEditForm):

    id = "CloudFrontSettings"
    label = _(u"CloudFront Settings")
    schema = ICloudFrontConfiguration
    # schema_prefix = 'collective.cloudfront.browser.interfaces.ICloudFrontConfiguration'
    schema_prefix = prefix


class CloudFrontControlPanel(controlpanel.ControlPanelFormWrapper):
    form = CloudFrontControlPanelForm
