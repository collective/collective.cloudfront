from zope.interface import Interface
from zope import schema
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.cloudfront')


class ICloudFrontConfiguration(Interface):
    distribution_id = schema.TextLine(
        title=_(u"label_distribution_id", default=u'Distribution ID'),
        description=_(
            u"help_distribution_id",
            default=u"Enter the AWS CloudFront distribution ID"
        ),
        required=True,
    )
    aws_access_key_id = schema.TextLine(
        title=_(u"label_aws_key_id", default=u'Access Key ID'),
        description=_(
            u"help_aws_key_id",
            default=u"Enter the AWS access key ID"
        ),
        required=True,
    )
    aws_secret_access_key = schema.TextLine(
        title=_(u"label_aws_secret", default=u'AWS Secret Access Key'),
        description=_(
            u"help_aws_secret",
            default=u"Enter the AWS secret access key"
        ),
        required=True,
    )
