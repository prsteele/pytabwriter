PyTabWriter
===========

A package for formatting text in aligned columns; inspired by Go's `text/tabwriter` [package](http://golang.org/pkg/text/tabwriter).

Example
-------

    >>> from pytabwriter import TabWriter
    >>> tw = TabWriter()
    >>> tw.writeln('first\tsecond\tthird')
    >>> tw.write('x\txx\txxx\n')
    >>> tw.write(['column 1', 'column 2', 'column 3'])
    >>> print(str(tw))
    first    second   third
    x        xx       xxx
    column 1 column 2 column 3
    >>> tw.alignment = 'r'
    >>> print(str(tw))
       first   second    third
           x       xx      xxx
    column 1 column 2 column 3
