=================
Setting a Favicon
=================

:Date: 2020-08-21 17:10
:Category: Features
:Tags: theme settings, favicon

kbits-theme lets you configure a custom favicon_ for your site via the
following theme settings:

.. _favicon: https://en.wikipedia.org/wiki/Favicon

``FAVICON_URL``
   A URL pointing to an image to use as the site's favicon.  If the URL is
   relative (does not begin with either ``http://`` or ``https://``), then
   ``{{SITEURL}}/`` is prepended to it.

``FAVICON_TYPE``
   The MIME type of the favicon image (``image/gif`` for a GIF, ``image/png``
   for a PNG, etc.).  Setting this is optional.
