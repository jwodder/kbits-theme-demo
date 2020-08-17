===================
The Navigation Pane
===================

:Date: 2020-08-17 17:34
:Category: Features
:Tags: navpane, theme settings
:Summary: See the list of links to the left?  This is all about that.

On the left side of every page of a kbits-theme site is the *navigation pane*,
a set of lists of links.  The contents of the pane are as follows:

- The main menu — Lists the items in ``MENUITEMS``, followed by the site's
  non-hidden pages if ``DISPLAY_PAGES_ON_MENU`` is true, followed by the site's
  categories if ``DISPLAY_CATEGORIES_ON_MENU`` is true

  - By default, the main menu is unlabelled, but a custom label can be
    displayed before the menu by setting the ``MENU_NAME`` setting.

- If ``PAGES_MENU`` is true and the site has any non-hidden pages, next is a
  list of the site's non-hidden pages.  This menu is labelled with the value of
  ``PAGES_MENU_NAME`` ("Pages" by default).

- If ``CATEGORIES_MENU`` is true and the site has any categories, next is a
  list of the site's categories.  This menu is labelled with the value of
  ``CATEGORIES_MENU_NAME`` ("Categories" by default).

- Next comes each of the lists defined by ``EXTRA_MENUS`` (`see below
  <EXTRA_MENUS_>`_)

- Finally, if ``FEED_ALL_ATOM``, ``FEED_ALL_RSS``, ``FEED_ATOM``, or
  ``FEED_RSS`` is set, links to the site's Atom and/or RSS feed are given.


Settings
========

The theme-specific settings that control the contents of the navigation pane
are as follows:

``MENU_NAME``
   The name to display above the main menu on the navigation pane.  Defaults to
   no name.

``MENUITEMS``
   A list of (Title, URL) pairs for additional menu items to appear at the
   beginning of the main menu in the navigation pane.  If a given URL is
   relative (does not begin with either ``http://`` or ``https://``), then
   ``{{SITEURL}}/`` is prepended to it.  This allows you to link to locations
   on your site without having to give the full URL.

``PAGES_MENU = False``
   If true, pages will be given their own menu in the navigation pane,
   after the main menu but before the categories menu and any menus defined
   with ``EXTRA_MENUS``.

``PAGES_MENU_NAME = "Pages"``
   The name to display above the pages menu (if there is one) on the
   navigation pane

``CATEGORIES_MENU = False``
   If true, categories will be given their own menu in the navigation pane,
   after the main menu and pages menu but before any menus defined with
   ``EXTRA_MENUS``.

``CATEGORIES_MENU_NAME = "Categories"``
   The name to display above the categories menu (if there is one) on the
   navigation pane

   .. _EXTRA_MENUS:

``EXTRA_MENUS``
   A list of (Menu Name, Link List) pairs defining extra lists of links to add
   to the navigation pane beneath all other menus.  Each "Link List" is a
   sublist of (Link Name, Link URL) pairs.

   If a given link URL is relative (does not begin with either ``http://`` or
   ``https://``), then ``{{SITEURL}}/`` is prepended to it.  This allows you to
   link to locations on your site without having to give the full URL.

   For example, the following setting:

   .. code:: python

       EXTRA_MENUS = [
           ('Social', [
               ('My Twitter', 'https://twitter.com/…'),
               ('My Mastodon', 'https://…'),
               ('My GitHub', 'https://github.com/…'),
           ]),
           ('Favorite Tags', [
               ('Python', 'tags/python.html'),
               ('Pelican', 'tags/pelican.html'),
           ]),
       ]

   causes the following to be added to the navigation pane on the left of the
   page::

        Social
        * My Twitter
        * My Mastodon
        * My GitHub

        Favorite Tags
        * Python
        * Pelican
