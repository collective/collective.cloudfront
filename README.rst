.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
collective.cloudfront
==============================================================================

AWS CloudFront support for plone.app.caching

This add-on watches for Purge notifications from ``plone.app.caching`` and sends the corresponding invalidation requests to an instance of Amazon’s CloudFront.


Features
--------

- Configurable in Site Setup (@@cloudfront-controlpanel)


Documentation
-------------

You will need to create an access key in your AWS Console.

Once you have the key’s ID and secret, you can provide them to your Plone site via Site Setup under “CloudFront Configuration”. You will also need to provide the ID for your CloudFront distribution.


Installation
------------

Install collective.cloudfront by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.cloudfront


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.cloudfront/issues
- Source Code: https://github.com/collective/collective.cloudfront


License
-------

The project is licensed under the GPLv2.
