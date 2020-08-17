===============
MathJax Support
===============

:Date: 2020-08-15 17:50
:Category: Features
:Tags: MathJax, reStructuredText, Markdown, theme settings
:Summary:
    Rendering things like :math:`\sum_{i=1}^n i = \frac{n^2+n}{2}` on your site

.. role:: rst(code)
    :language: rst

.. role:: tx(code)
    :language: tex

kbits-theme has built-in support for MathJax_; with a single setting, the theme
will enable it on every page of the themed site.  That's just the first step in
getting MathJax to work, though, and the remainder of the required steps depend
on what markup format you're working with.

.. _MathJax: https://www.mathjax.org


MathJax Settings
================

kbits-theme's MathJax support can be controlled with the following Pelican
settings:

``USE_MATHJAX = False``
   Set to ``True`` to enable MathJax on every page of the site

``MATHJAX_SCRIPT = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"``
   Set the MathJax script to load.  The default setting loads the tex-chtml__
   component from the latest revision of MathJax version 3.

   __ http://docs.mathjax.org/en/latest/web/components/combined.html#tex-chtml

``MATHJAX_CONFIG = {}``
   Set configuration settings for MathJax.  Configuration is applied assuming
   version 3 of MathJax is in use.  Only JSON-serializable values are supported
   in ``MATHJAX_CONFIG``.


MathJax with reStructuredText
=============================

To be able to produce mathematical output with MathJax while writing in
reStructuredText, you need to set the ``"math_output"`` key of your Pelican
site's ``DOCUTILS_SETTINGS`` setting to ``"mathjax irrelevant-value"``.  The
"mathjax" part is case insensitive.  The second word in the string doesn't
matter, but it needs to be there to prevent Docutils from emitting a warning
that makes Pelican halt.  After you've made this change, any use of the |math
role| or `"math" directive`_ in your documents will produce output that MathJax
will then render into mathematical notation.

.. note::

    When using the "math" directive, Docutils will wrap your math markup in a
    :tx:`\begin{align*}` ... :tx:`\end{align*}` environment if it contains any
    :tx:`\\` commands outside of an environment, and in a
    :tx:`\begin{equation*}` ... :tx:`\end{equation*}` environment otherwise.

.. |math role| replace:: :rst:`:math:` role
.. _math role: https://docutils.sourceforge.io/docs/ref/rst/roles.html#math

.. _"math" directive:
   https://docutils.sourceforge.io/docs/ref/rst/directives.html#math


MathJax with Markdown
=====================

For writing math in Markdown with kbits-theme, the best option appears to be
the pymdown-extensions_ package and its Markdown extension Arithmatex_, which
can convert math markup in Markdown input into MathJaxable output.  In order to
use this extension with kbits-theme, you must install pymdown-extensions into
your Pelican environment and set Arithmatex's "generic" option to true by
adding the following configuration to your Pelican site's ``MARKDOWN`` setting:

.. code:: python

    MARKDOWN = {
        ...
        "extension_configs": {
            ...
            "pymdownx.arithmatex": {"generic": True},
            ...
        },
        ...
    }

If this is the first time you're modifying the value of ``MARKDOWN``, you
should copy the default value shown in `the Pelican documentation`__ and modify
that.

__ https://docs.getpelican.com/en/stable/settings.html

An alternative worth mentioning is the pelican-render-math_ plugin for Pelican,
which enables writing math in Markdown and adds a ``<script>`` tag for
activating MathJax to the end of any rendered reStructuredText or Markdown
content that includes math markup.  This ``<script>`` conflicts with the
MathJax loaded by kbits-theme, so if you're using pelican-render-math, it's
recommended to leave ``USE_MATHJAX`` at ``False`` and configure MathJax through
pelican-render-math's facilities instead.  Also note that the plugin requires
the next version of Pelican after 4.2, which at time of writing has not yet
been released.

Another alternative, mentioned here for completeness' sake, is the
python-markdown-math_ package.  The output it produces is by default only
compatible with version 2 of MathJax, so if you use it with kbits-theme, you
will need to set ``MATHJAX_SCRIPT`` to a version 2 URL, and ``MATHJAX_CONFIG``
will be unusable.

.. _pymdown-extensions: https://github.com/facelessuser/pymdown-extensions
.. _Arithmatex:
   https://facelessuser.github.io/pymdown-extensions/extensions/arithmatex/
.. _pelican-render-math: https://github.com/pelican-plugins/render-math
.. _python-markdown-math: https://github.com/mitya57/python-markdown-math


Other Considerations
====================

If you're using MathJax and Typogrify is enabled for your site, and if you're
not using pelican-render-math (which takes care of this automatically), you
need to configure Typogrify to ignore math tags.  Add ``".math"`` to your
site's ``TYPOGRIFY_IGNORE_TAGS`` setting if you're writing math in
reStructuredText, add ``".arithmatex"`` if you're writing in Markdown with
pymdown-extensions' Arithmatex, and add ``"script"`` if you're writing in
Markdown with python-markdown-math.  Typogrify v2.0.7 or higher is required for
such settings.


Some MathJax Output
===================

But enough about all that.  You came here to see some math, didn't you?
Behold!

.. topic:: Theorem

    For all positive integers :math:`n`, :math:`\sum_{i=1}^n i =
    \frac{n^2+n}{2}`.

    **Proof:** When :math:`n = 1`, then:

    .. math::

        \sum_{i=1}^n i & = \sum_{i=1}^1 i \\
                       & = 1 \\
                       & = \frac{1^2+1}{2} \\
                       & = \frac{n^2+n}{2}

    If :math:`\sum_{i=1}^n i = \frac{n^2+n}{2}` for some positive integer
    :math:`n`, then:

    .. math::

        \sum_{i=1}^n i & = \frac{n^2+n}{2} \\
        \left(\sum_{i=1}^n i\right) + (n+1) & = \frac{n^2+n}{2} + (n+1) \\
        \sum_{i=1}^{n+1} i & = \frac{n^2+n + 2n + 2}{2} \\
                           & = \frac{(n^2+2n+1) + (n+1)}{2} \\
                           & = \frac{(n+1)^2 + (n+1)}{2}

    and so the statement holds for :math:`n+1` as well.
    
    Therefore, by the Principle of Mathematical Induction, :math:`\sum_{i=1}^n
    i = \frac{n^2+n}{2}` for all positive integers :math:`n`.  ∎
