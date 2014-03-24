#!/usr/bin/env python
from distutils.core import setup

setup(name = 'parsedom',
      version = '1.0.0',
      author = 'Thomas Amland',
      author_email = 'thomas.amland@googlemail.com',
      url = "https://github.com/tamland/parsedom",
      license = 'GPLv3',
      description = 'A fast DOM parser',
      long_description = open('README.rst').read(),
      packages = ['parsedom'],
      classifiers = ["Development Status :: 5 - Production/Stable",
                     "Programming Language :: Python",
                     "Operating System :: OS Independent",
                     "Topic :: Text Processing :: Markup :: HTML",
                     "Topic :: Text Processing :: Markup :: XML",
                     "Topic :: Software Development :: Libraries :: Python Modules"],
)
