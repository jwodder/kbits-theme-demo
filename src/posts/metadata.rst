=======================
Article Metadata Tables
=======================

:Date: 2020-08-16 16:28
:Category: Features
:Tags: articles, metadata, theme settings
:Formatted Field: The <tag> in **bold**
:Unformatted Field: The <tag> in **bold**

.. role:: rst(code)
    :language: rst

At the top of each article in a kbits-theme site, just underneath the article
title, kbits-theme displays a table of the article's metadata.  (Look right
above this paragraph for an example.)  By default, the following fields are
shown:

- Date (labelled "Posted")
- Modified (if set; labelled "Last Updated")
- Author(s)
- Category
- Tags (If there are no tags, "—" is shown)
- Translations (if there are any)

The metadata table can be configured via the following theme settings:

``SHOW_AUTHOR``
   If this is set to ``False`` (default value: ``True``), the author(s) field
   will be omitted from articles' metadata tables.  This is useful if your site
   only has one author and you don't want to slap your name all over
   everything.

``GITHUB_SOURCE_URL``
   If your site's repository is hosted on GitHub, setting this variable to
   the repository's URL (in the form ``"https://github.com/$OWNER/$REPO"``,
   without trailing ``.git``) will add a "Page Source" entry to each article's
   metadata table pointing to the article source file on GitHub.  Setting this
   value also requires setting ``PATH_IN_REPO``.

``GITHUB_SOURCE_BRANCH = "master"``
   The branch of the ``GITHUB_SOURCE_URL`` repository on which the site's
   source is located.

``PATH_IN_REPO``
   The ``/``-separated path to your content directory, relative to the root of
   your repository.  This will usually be equal to ``PATH``.  This needs to be
   set whenever ``GITHUB_SOURCE_URL`` is set.

``EXTRA_METADATA_FIELDS``
   A list of (Field Name, Article Attribute) pairs specifying additional
   metadata fields to list in articles' metadata tables.  The "Field Name" is
   the text to label the field with in the table (minus the colon which will be
   automatically appended), and the "Article Attribute" is the name of the
   field as available as an attribute of an ``Article`` object (i.e., the name
   of the field as written in your document metadata, but converted to
   all-lowercase).  If a given field is empty or not set on an article, it is
   not listed in that article's metadata table.

   For example, if you include an "``:ORCID:``" field in the docinfo of your
   articles, you can include ``("Author ORCID", "orcid")`` in
   ``EXTRA_METADATA_FIELDS`` to cause the field to be listed in the metadata
   table with a label of "Author ORCID:".

   Field values will be HTML-escaped unless the "Article Attribute" is listed
   in ``FORMATTED_FIELDS``.  An example of a formatted field and an unformatted
   field can be seen above in this article's metadata table; the value for both
   fields is written as :rst:`The <tag> in **bold**` in the document source.

   .. note::

       When writing in reStructuredText, Pelican always treats the built-in
       `bibliographic fields`_ as unformatted (aside from "abstract" and
       "dedication", which are removed from the fields list by the time Pelican
       processes the document).  Including them in ``FORMATTED_FIELDS`` can
       thus cause kbits-theme to do the wrong thing.

   .. note::

       As of Pelican 4.2, when writing in reStructuredText, field names are
       compared case sensitively against the elements of ``FORMATTED_FIELDS``.
       This means that, if you want to write :rst:`:Some Field Name: *value*`
       in your documents and have :rst:`*value*` be formatted in the metadata
       table, you need to include both ``"Some Field Name"`` (so that Pelican
       will format the field) and ``"some field name"`` (so that kbits-theme
       will know that the field is formatted) in your site's
       ``FORMATTED_FIELDS`` value.

       This does not apply to Markdown, where the elements of
       ``FORMATTED_FIELDS`` are expected to be all-lowercase and field names in
       source documents are lowercased before comparison.

       `PR #2785`_ changed the handling of ``FORMATTED_FIELDS`` for
       reStructuredText documents to match that of Markdown documents, but at
       time of writing a Pelican release with this patch has not yet been made.

.. _bibliographic fields:
   https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html
   #bibliographic-fields

.. _PR #2785: https://github.com/getpelican/pelican/pull/2785
