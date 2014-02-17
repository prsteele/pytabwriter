import unittest

from pytabwriter import TabWriter

class TestTabWriter(unittest.TestCase):
    """Unit tests for the TabWriter class.

    """

    def setUp(self):
        """Create a TabWriter for testing."""

        self.tw = TabWriter()

    def test_padding_property(self):
        """Test the padding property."""

        for x in [0, 10, [1] * 10]:
            self.tw.padding = x
            self.assertEqual(self.tw.padding, x)

        for x in [-1, [-1, 1], 'text']:
            with self.assertRaises(ValueError):
                self.tw.padding = x

    def test_alignment_property(self):
        """Test the alignment property."""

        for x in ['l', 'c', 'r', ['l', 'c', 'r']]:
            self.tw.alignment = x
            self.assertEqual(self.tw.alignment, x)

        for x in [0, 't', ['t']]:
            with self.assertRaises(ValueError):
                self.tw.alignment = x

    def test_padchar_property(self):
        """Test the padchar property."""

        for c in ['', ' ', 'x', [' ', 'x']]:
            self.tw.padchar = c
            self.assertEqual(self.tw.padchar, c)

        for c in [0, 1, 2]:
            self.tw.padchar = c
            self.assertEqual(self.tw.padchar, str(c))

        for x in ['  ', 'text', 10, ['  ', ' ']]:
            with self.assertRaises(ValueError):
                self.tw.padchar = x

    def test_tabchar_property(self):
        """Test the tabchar property."""

        for c in ['\t', ' ', '-', 'x', 'whynot']:
            self.tw.tabchar = c
            self.assertEqual(self.tw.tabchar, c)

        for c in [0, 1, 2]:
            self.tw.tabchar = c
            self.assertEqual(self.tw.tabchar, str(c))

        with self.assertRaises(ValueError):
            self.tw.tabchar = ''

    def test_write_1(self):
        """Test the write method."""

        msg = 'a\tb\tc\naa\tbb\tcc'
        out = '\n'.join(['a  b  c  ',
                         'aa bb cc '])

        self.tw.write(msg)
        self.assertEqual(str(self.tw), out)

    def test_write_2(self):
        """Test the write method, with padding."""

        msg = 'a\tb\tc\naa\tbb\tcc'
        out = '\n'.join(['a   b   c   ',
                         'aa  bb  cc  '])
        self.tw.padding = 2

        self.tw.write(msg)
        self.assertEqual(str(self.tw), out)
        
    def test_write_3(self):
        """Test the write method, with alignment."""

        msg = 'a\tb\tc\naa\tbb\tcc'
        out = '\n'.join(['  a  b  c',
                         ' aa bb cc'])
        self.tw.alignment = 'r'

        self.tw.write(msg)
        self.assertEqual(str(self.tw), out)
                
    def test_write_4(self):
        """Test the write method, with list padding."""

        msg = 'a\tb\tc\naa\tbb\tcc'
        out = '\n'.join(['a b  c   ',
                         'aabb cc  '])
        self.tw.padding = [0, 1, 2]

        self.tw.write(msg)
        self.assertEqual(str(self.tw), out)

    def test_write_5(self):
        """Test the write method, with list alignment."""

        msg = 'a\tb\tc\naa\tbb\tcc'
        out = '\n'.join(['a   b   c',
                         'aa bb  cc'])
        self.tw.alignment = ['l', 'c', 'r']

        self.tw.write(msg)
        self.assertEqual(str(self.tw), out)

    def test_writeln(self):
        """Test the writeln method."""
        
        out = '\n'.join(['a  b  c  ',
                         'aa bb cc '])

        self.tw.writeln('a\tb\tc')
        self.tw.writeln('aa\tbb\tcc')
        self.assertEqual(str(self.tw), out)

    def test_clear(self):
        """Test the clear method."""
        
        out = '\n'.join(['a  b  c  ',
                         'aa bb cc '])

        self.tw.writeln('a\tb\tc')
        self.tw.writeln('aa\tbb\tcc')
        self.assertEqual(str(self.tw), out)

        self.tw.clear()
        
        self.tw.writeln('a\tb\tc')
        self.tw.writeln('aa\tbb\tcc')
        self.assertEqual(str(self.tw), out)
