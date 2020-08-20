==============================================
Table Styles and Alignment in reStructuredText
==============================================

:Date: 2020-08-13 22:54
:Category: Features
:Tags: reStructuredText, styles, tables
:Summary:
    kbits-theme's support for Docutils table styles and table alignment
    specifiers

Did you know?  The default stylesheet bundled with Docutils (the standard
renderer for reStructuredText) supports two special class values for tables,
"``booktabs``" and "``borderless``", and kbits-theme supports them as well.
kbits-theme also includes support for alignment of tables in the center or at
the right edge of a page.

When writing in reStructuredText, one can set the class for a table using the
`"class" directive`_ or the ``:class:`` option of the `"table" directive`_.
Alternatively, a table can be expressed using the `"csv-table" directive`_ or
`"list-table" directive`_, both of which support the ``:class:`` option.

If a table is given the "``booktabs``" class, the only rules in the table will
be two slightly thick rules at the top & bottom of the table and a thin rule
after the head, like so:

.. table::
    :class: booktabs

    ======  =======
    Color   Element
    ======  =======
    Blue    Water
    Green   Earth
    Red     Fire
    Yellow  Air
    ======  =======

If the table is instead given the "``borderless``" class, it will not have any
rules at all, like so:

.. table::
    :class: borderless

    ======  =======
    Color   Element
    ======  =======
    Blue    Water
    Green   Earth
    Red     Fire
    Yellow  Air
    ======  =======

The three table directives also support an ``:align:`` option, which can be set
to "``left``", "``center``", or "``right``" to cause the table to be
left-aligned, centered, or right-aligned.  For example, a centered table:

.. table::
    :align: center

    ======  =======
    Color   Element
    ======  =======
    Blue    Water
    Green   Earth
    Red     Fire
    Yellow  Air
    ======  =======

and a right-aligned table:

.. table::
    :align: right

    ======  =======
    Color   Element
    ======  =======
    Blue    Water
    Green   Earth
    Red     Fire
    Yellow  Air
    ======  =======

Note that, unlike in HTML documents styled with Docutils' default stylesheet,
the text inside aligned tables is always left-aligned (or centered, for
headers) rather than matching the alignment of the table.  This is a deliberate
design choice by kbits-theme.

.. _"class" directive:
   https://docutils.sourceforge.io/docs/ref/rst/directives.html#class

.. _"table" directive:
   https://docutils.sourceforge.io/docs/ref/rst/directives.html#table

.. _"csv-table" directive:
   https://docutils.sourceforge.io/docs/ref/rst/directives.html#id4

.. _"list-table" directive:
   https://docutils.sourceforge.io/docs/ref/rst/directives.html#list-table
