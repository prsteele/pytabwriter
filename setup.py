from distutils.core import setup

desc = '\n'.join(['A module for writing formatted columns of text.',
                  'See https://github.com/prsteele/pytabwriter for details'])

setup(
    name='PyTabWriter',
    version='0.1.1',
    packages=['pytabwriter'],
    license='BSD 3-clause license',
    long_description=desc,
    author='Patrick Steele',
    author_email='steele.pat@gmail.com',
    url='https://github.com/prsteele/pytabwriter'
)
