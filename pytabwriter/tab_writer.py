class TabWriter:
    """A class for creating formatted columns of text.

    """

    def __init__(self):
        self.buffer = []
        self._strings = []
        self._padding = 1
        self._padchar = ' '
        self._alignment = 'l'

    @property
    def padding(self):
        return self._padding

    @padding.setter
    def padding(self, p):
        self._padding = p

    @property
    def alignment(self):
        return self._alignment

    @alignment.setter
    def alignment(self, align):
        if align not in ['l', 'c', 'r']:
            msg = 'Invalid alignment character: {}'.format(str(align))
            raise ValueError(msg)
        
        self._alignment = align

    def write(self, x):
        """Add text to the output buffer.

        Parameters
        ----------

        x : string or list
            If a string, additional text for the output buffer. If a
            list, it is interpreted as a sequence of columns in a row.

        """

        if isinstance(x, list):
            self._process_strings()
            self.buffer.append(x)
        else:
            self._strings.append(str(x))

    def _process_strings(self):
        """Split the current input line by newline characters and add each
        line to the buffer.

        """

        if len(self._strings) == 0:
            return

        text = ''.join(self._strings)
        self.buffer.extend(line.split('\t') for line in text.split('\n'))
        self._strings = []

    def __str__(self):
        """Return a string representation of all the text written to the
        TabWriter with column formatting applied.

        """

        # Get the width of each column
        columns = max(len(row) for row in self.buffer)
        column_widths = [0] * columns
        for row in self.buffer:
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
        for row in self.buffer:
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
