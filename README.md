PyTabWriter
===========

A package for formatting text in aligned columns; inspired by Go's `text/tabwriter` [package](http://golang.org/pkg/text/tabwriter).

Example
-------

You can form columns by inserting literal tab characters where columns
should go.

    >>> tw = TabWriter()
    >>> tw.write('First\tsecond\tthird\n')
    >>> tw.write('x\txx\txxx\n')
    >>> print(str(tw))
    First second third
    x     xx     xxx
    >>> tw.padding = 2
    >>> print(str(tw))
    First  second  third
    x      xx      xxx
    >>> tw.column_align = ['l', 'c', 'r']
    >>> print(str(tw))
    First  second  third
    x        xx      xxx
    
You can also pass in lists of entries, one per row.

    >>> tw = TabWriter()
    >>> tw.write(['First', 'second', 'third'])
    >>> tw.write(['x', 'xx', 'xx'])
    >>> print(str(tw))
    First second third
    x     xx     xxx
