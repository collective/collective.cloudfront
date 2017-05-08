import logging
from time import time

from plone.registry.interfaces import IRegistry
from zope.component import getUtility

import boto3


# TODO fix firing of Purge and submit pull request
# TODO create control panel for AWS credentials and distribution ID

logger = logging.getLogger('sixfeetup.cloudfrontpurging')

def purge_cache(content_obj, event):
    url = content_obj.absolute_url_path()
    registry = getUtility(IRegistry)
    distribution_id = registry['sixfeetup.cloudfrontpurging.distribution_id']
    if not distribution_id:
        logger.error('Please provide a CloudFront Distribution ID')
        return
    reference = 'plonepurge' + str(time())
    cloudfront = boto3.client('cloudfront')
    try:
        response = cloudfront.create_invalidation(
            DistributionId=distribution_id,
            InvalidationBatch={
                'Paths': {
                    'Quantity': 1,
                    'Items': [url],
                },
                'CallerReference': reference,
            }
        )
        i_id = response['Invalidation']['Id']
        i_url = response['Location']
        logger.info('Invalidated %s with ID %s', i_url, i_id)
    except Exception as e:
        logger.warn('Invalidation request failed for %s: %s', url, e.message)
