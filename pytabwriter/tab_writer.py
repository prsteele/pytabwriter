class TabWriter:
    """A class for creating formatted columns of text.

    """

    def __init__(self, **kwds):
        """Construct a new TabWriter.

        Keyword arguments
        -----------------

        padding : int or list
            Sets the padding property

        alignment : str or list
            Sets the alignment property

        padchar : str or list
            Sets the padchar property
        
        tabchar : str or list
            Sets the tabchar property

        Usage
        -----

        A TabWriter object acts as a buffer for a number of calls to
        the `write` method. To access the formatted str output of a
        number of these calls, convert the TabWriter using the `str`
        method.

        Properties
        ----------

        Several properties (padding, alignment, padchar) accept both
        single values and lists of values; when a single value is
        supplied it is used for all columns, and when a list is
        supplied the values are used in order for each column, cycling
        the list as necessary.

        """

        # A list of rows, where each row is a list of columns
        self._buffer = []

        # A list of strings that have not been processed into _buffer
        self._strings = []

        # These fields are controlled by properties
        self.padding = kwds.pop('padding', 1)
        self.padchar = kwds.pop('padchar', ' ')
        self.alignment = kwds.pop('alignment', 'l')
        self.tabchar = kwds.pop('tabchar', '\t')

        if len(kwds) > 0:
            unknown = list(kwds.keys())
            msg = 'Unknown keyword arguments: {}'.format(str(unknown))
            raise TypeError(msg)

    @property
    def padding(self):
        return self._padding

    @padding.setter
    def padding(self, p):

        if isinstance(p, list):
            p = [int(x) for x in p]

            if any([x < 0 for x in p]):
                raise ValueError('Padding must be nonnegative')
        else:
            p = int(p)

            if p < 0:
                raise ValueError('Padding must be nonnegative')

        self._padding = p

    @property
    def alignment(self):
        """This property controls the alignment of columns. Valid values are
        'l', 'c', or 'r', for left, center, and right alignment,
        respectively. A list of such values can be supplied to control
        each column individually.

        """
        
        return self._alignment

    @alignment.setter
    def alignment(self, align):

        """setter"""
        valid = ['l', 'c', 'r']
        msg = 'Invalid alignment character: {}'

        if isinstance(align, list):
            for c in align:
                if c not in valid:
                    raise ValueError(msg.format(c))
        else:
            if align not in valid:
                msg.format(str(align))
                raise ValueError(msg)
        
        self._alignment = align

    @property
    def padchar(self):
        """This property controls what character is used for padding
        columns. Valid values are any str of length 1. A list of such
        values may be used to control each column individually.

        """
        
        return self._padchar

    @padchar.setter
    def padchar(self, c):
        msg = 'Pad string must be at most one character long'
        
        if isinstance(c, list):
            c = [str(x) for x in c]

            if any([len(x) > 1 for x in c]):
                   raise ValueError(msg)
        else:
            c = str(c)
            if len(c) > 1:
                raise ValueError(msg)

        self._padchar = c

    @property
    def tabchar(self):
        """This property controls what character is used for delimiting
        columns. Valid values are any str of length 1. The default
        value is the tab character '\t'.

        """
        
        return self._tabchar

    @tabchar.setter
    def tabchar(self, c):
        c = str(c)

        if len(c) == 0:
            raise ValueError('The tab string must be nonempty')
                   
        self._tabchar = c

    def write(self, x):
        """Add text to the output buffer.

        Parameters
        ----------

        x : str or list
            If a str is provided it is appended to the output
            buffer. If a list is provided, it is interpreted as a
            sequence of columns in a single row; the output buffer is
            assumed to begin a line at the start of this row and begin
            a line after this row.

        """

        if isinstance(x, list):
            self._process_strings()
            self._buffer.append(x)
        else:
            self._strings.append(str(x))

    def writeln(self, x):
        """Add a row of text to the output buffer.

        Parameters
        ----------

        x : str
            A row (or rows) of text to be added to the output
            buffer. This text will begin on the line after the
            existing buffer text, and subsequent calls to `write` or
            `writeln` will begin on a line after this text.

        """

        self._process_strings()
        self._strings.append(str(x))
        self._process_strings()

    def _process_strings(self):
        """Split the current input line by newline characters and add each
        line to the buffer.

        """

        if len(self._strings) == 0:
            return

        text = ''.join(self._strings)
        self._buffer.extend(line.split('\t') for line in text.split('\n'))
        self._strings = []

    def __str__(self):
        """Return a string representation of all the text written to the
        TabWriter with column formatting applied.

        """

        self._process_strings()

        # Get the width of each column
        columns = max(len(row) for row in self._buffer)
        column_widths = [0] * columns
        for row in self._buffer:
            for (i, col) in zip(range(columns), row):
                w = len(col)
                if w > column_widths[i]:
                    column_widths[i] = w

        # Get the padding for each column
        if isinstance(self.padding, int):
            padding = [self.padding] * columns
        else:
            padding = self.padding + [1] * (columns - len(self.padding))

        # Get the alignment for each column
        if isinstance(self.alignment, str):
            alignment = [self.alignment] * columns
        else:
            alignment = self.alignment + ['l'] * (columns - len(self.alignment))


        lines = []
        for row in self._buffer:
            cols = []
            for (i, col) in zip(range(columns), row):
                pad = self._padchar * (column_widths[i] - len(col) + padding[i])
                if alignment[i] == 'l':
                    entry = col + pad
                elif alignment[i] == 'c':
                    entry = pad[:len(pad) // 2] + col + pad[len(pad) // 2:]
                else:
                    entry = pad + col
                cols.append(entry)
            lines.append(''.join(cols))

        return '\n'.join(lines)

    def clear(self):
        """Clear all data written so far."""

        self._buffer = []
        self._strings = []
