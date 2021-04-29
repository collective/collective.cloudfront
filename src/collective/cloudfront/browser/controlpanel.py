from collective.cloudfront import (
    _,
    events,
    prefix,
)
from .interfaces import ICloudFrontConfiguration
from logging import getLogger
from plone import api
from plone.app.registry.browser import controlpanel
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.statusmessages.interfaces import IStatusMessage

log = getLogger('Plone')


class CloudFrontControlPanelForm(controlpanel.RegistryEditForm):

    id = "CloudFrontSettings"
    label = _(u"CloudFront Settings")
    schema = ICloudFrontConfiguration
    # schema_prefix = 'collective.cloudfront.browser.interfaces.ICloudFrontConfiguration'
    schema_prefix = prefix


class CloudFrontControlPanel(controlpanel.ControlPanelFormWrapper):
    form = CloudFrontControlPanelForm
    index = ViewPageTemplateFile('settings.pt')


class PurgeCache(BrowserView):

    def __call__(self):
        portal = api.portal.get()
        messages = IStatusMessage(self.request)
        msg = events.purge_cache(portal, None)
        messages.add(msg, type=u"info")
        cp_url = api.portal.get().absolute_url() + '/@@cloudfront-controlpanel'
        self.request.response.redirect(cp_url)
