from plone import api

def upgrade_rolemap(context):
    # set up roles for managePurging
    setup = api.portal.get_tool('portal_setup')
    setup.runImportStepFromProfile('collective.cloudfront:initial', 'rolemap')
