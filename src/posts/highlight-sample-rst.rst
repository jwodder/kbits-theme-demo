=========================================
Syntax Highlighting with reStructuredText
=========================================

:Date: 2020-08-20 18:03
:Category: Examples
:Tags: reStructuredText, styles, syntax highlighting

.. role:: py(code)
    :language: python

kbits-theme uses Pygments' "default" style for code syntax highlighting.  Let's
see some examples!

reStructuredText has a built-in directive for syntax highlighting, the `"code"
directive`_.  Here's what the output of that directive looks like in
kbits-theme:

.. code:: python

    from itertools import compress

    def subsets(xs, nonempty=False, proper=False):
        """
        Returns an iterator over all subsets of the iterable ``xs`` as tuples.
        If ``nonempty`` is true, only nonempty subsets are returned.  If
        ``proper`` is true, only proper subsets are returned.
        """
        xs = tuple(xs)
        selectors = [False] * len(xs)
        while True:
            if not (
                (nonempty and not any(selectors)) or (proper and all(selectors))
            ):
                yield tuple(compress(xs, selectors))
            for i in xrange(len(selectors)):
                selectors[i] = not selectors[i]
                if selectors[i]:
                    break
            else:
                break

... and here's what it looks like with the ``:number-lines:`` option:

.. code:: python
    :number-lines:

    from itertools import compress

    def subsets(xs, nonempty=False, proper=False):
        """
        Returns an iterator over all subsets of the iterable ``xs`` as tuples.
        If ``nonempty`` is true, only nonempty subsets are returned.  If
        ``proper`` is true, only proper subsets are returned.
        """
        xs = tuple(xs)
        selectors = [False] * len(xs)
        while True:
            if not (
                (nonempty and not any(selectors)) or (proper and all(selectors))
            ):
                yield tuple(compress(xs, selectors))
            for i in xrange(len(selectors)):
                selectors[i] = not selectors[i]
                if selectors[i]:
                    break
            else:
                break

Pelican provides a more featureful alternative to "code", the `"code-block"
directive`_.  The default output is pretty much the same as that of "code", but
if we enable table-style line numbers with the ``:linenos:`` option, we see a
difference:

.. code-block:: python
    :linenos:

    from itertools import compress

    def subsets(xs, nonempty=False, proper=False):
        """
        Returns an iterator over all subsets of the iterable ``xs`` as tuples.
        If ``nonempty`` is true, only nonempty subsets are returned.  If
        ``proper`` is true, only proper subsets are returned.
        """
        xs = tuple(xs)
        selectors = [False] * len(xs)
        while True:
            if not (
                (nonempty and not any(selectors)) or (proper and all(selectors))
            ):
                yield tuple(compress(xs, selectors))
            for i in xrange(len(selectors)):
                selectors[i] = not selectors[i]
                if selectors[i]:
                    break
            else:
                break

The "code-block" directive also lets us highlight individual lines with the
``:hl_lines:`` option:

.. code-block:: python
    :linenos:
    :hl_lines: 12 13 14 15

    from itertools import compress

    def subsets(xs, nonempty=False, proper=False):
        """
        Returns an iterator over all subsets of the iterable ``xs`` as tuples.
        If ``nonempty`` is true, only nonempty subsets are returned.  If
        ``proper`` is true, only proper subsets are returned.
        """
        xs = tuple(xs)
        selectors = [False] * len(xs)
        while True:
            if not (
                (nonempty and not any(selectors)) or (proper and all(selectors))
            ):
                yield tuple(compress(xs, selectors))
            for i in xrange(len(selectors)):
                selectors[i] = not selectors[i]
                if selectors[i]:
                    break
            else:
                break

... or make every *n*-th line number stand out:

.. code-block:: python
    :linenos:
    :linenospecial: 5

    from itertools import compress

    def subsets(xs, nonempty=False, proper=False):
        """
        Returns an iterator over all subsets of the iterable ``xs`` as tuples.
        If ``nonempty`` is true, only nonempty subsets are returned.  If
        ``proper`` is true, only proper subsets are returned.
        """
        xs = tuple(xs)
        selectors = [False] * len(xs)
        while True:
            if not (
                (nonempty and not any(selectors)) or (proper and all(selectors))
            ):
                yield tuple(compress(xs, selectors))
            for i in xrange(len(selectors)):
                selectors[i] = not selectors[i]
                if selectors[i]:
                    break
            else:
                break


.. TODO: "code" role

reStructuredText also provides a |code role|_ that can be used for highlighting
inline code samples.  To use it, first create a "subrole" with the name of the
highlighted language supplied to the ``:language:`` option:

.. code:: rst

    .. role:: py(code)
        :language: python

... and then you can write this:

.. code:: rst

    Put :py:`"2" * 2` in the REPL to get :py:`"22"`.

... to get this:

    Put :py:`"2" * 2` in the REPL to get :py:`"22"`.

.. _"code" directive:
   https://docutils.sourceforge.io/docs/ref/rst/directives.html#code

.. _"code-block" directive:
   https://docs.getpelican.com/en/stable/content.html#syntax-highlighting

.. |code role| replace:: ``:code:`` role
.. _code role: https://docutils.sourceforge.io/docs/ref/rst/roles.html#code
