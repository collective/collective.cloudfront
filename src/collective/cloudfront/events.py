import logging
from time import time

from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from collective.cloudfront import prefix

import boto3


logger = logging.getLogger('collective.cloudfront')


def get_cloudfront_settings():
    registry = getUtility(IRegistry)
    setting_keys = (
        'distribution_id',
        'aws_access_key_id',
        'aws_secret_access_key',
    )
    return {sk: registry['{}.{}'.format(prefix, sk)] for sk in setting_keys}


def purge_cache(content_obj, event):
    url = content_obj.absolute_url_path()
    if url == '/':
        url = '/*'
    cloudfront_prefs = get_cloudfront_settings()
    if not all(cloudfront_prefs.values()):
        msg = 'Please provide CloudFront settings in the Control Panel'
        logger.error(msg)
        return msg
    reference = 'plonepurge' + str(time())
    cloudfront = boto3.client(
        'cloudfront',
        aws_access_key_id=cloudfront_prefs['aws_access_key_id'],
        aws_secret_access_key=cloudfront_prefs['aws_secret_access_key'],
    )
    try:
        response = cloudfront.create_invalidation(
            DistributionId=cloudfront_prefs['distribution_id'],
            InvalidationBatch={
                'Paths': {
                    'Quantity': 1,
                    'Items': [url],
                },
                'CallerReference': reference,
            }
        )
        i_id = response['Invalidation']['Id']
        msg = 'Invalidated {0} with ID {1}'.format(url, i_id)
        logger.info(msg)
        return msg
    except Exception as e:
        msg = 'Invalidation request failed for {0}: {1}'.format(url, e.message)
        logger.warn(msg)
        return msg
