Article with Mathematical Content
=================================

:date: 2020-07-31
:summary: Here we prove that :math:`\sum_{i=1}^n i = \frac{n^2+n}{2}`

.. TODO: Insert details on using MathJax with kbits-theme

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
